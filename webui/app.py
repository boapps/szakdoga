from flask import Flask
import requests
import newspaper
import sys
import json
import feedparser
from threading import Thread
import time
import traceback
import Article
import json_fix
import pickle
from flask import request
import csv
import lm_dataformat

LLM_SERVER = 'http://127.0.0.1:8085'

# TODO: sqlite db

# list of urls that we once added to queue
seen: [str] = []

# all articles that we think are corruption related (positive)
articles: [Article.Article] = []

# articles queued for processing
article_queue: [Article.Article] = []

article_classification_prompt = '''[korrupció klasszifikáció]
{title}

{description}

{text}

cimkék: {keywords}

###

téma:'''


def save_state():
    articles.sort(reverse=True, key=lambda a: a.date)
    #print('save')

    with open('articles', 'wb') as articles_file:
        pickle.dump(articles, articles_file)

    with open('article_queue', 'wb') as queue_file:
        pickle.dump(article_queue, queue_file)

    with open('seen', 'wb') as seen_file:
        pickle.dump(seen, seen_file)

def load_file(name: str):
    try:
        with open(name, 'rb') as data_file:
            data = pickle.load(data_file)
            print('loaded', len(data), name)
    except IOError:
        data = []
    return data

def load_state():
    print('loading state...')
    articles = load_file('articles')
    seen = load_file('seen')
    article_queue = load_file('article_queue')

    return articles, seen, article_queue

def init_seen():
    for feed_url in feed_urls:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            if entry.link not in seen:
                seen.append(entry.link)

def rss_watcher():
    while True:
        #print('running rss watcher loop')
        for feed_url in feed_urls:
            get_new_from_rss(feed_url)
            save_state()
        #print('rss watcher loop done')
        time.sleep(5*60)

def article_processor():
    while True:
        #print('running article processor loop')
        while len(article_queue) > 0:
            process(article_queue.pop())
            save_state()
            print('articles left:', len(article_queue))
        #print('article processor loop done')
        time.sleep(1*60)

def get_new_from_rss(url):
    articles_found = 0
    articles_skipped = 0
    feed = feedparser.parse(url)
    for entry in feed.entries:
        if entry.link not in seen:
            if any(entry.link.startswith(url_pattern) for url_pattern in skip_url_patterns):
                seen.append(entry.link)
                articles_skipped += 1
                continue

            try:
                article_queue.append(Article.Article(entry.link))
                articles_found += 1
            except newspaper.ArticleException:
                traceback.print_exc()
            finally:
                seen.append(entry.link)
                time.sleep(3)
    # TODO: sorting
    if articles_found > 0:
        print(url, 'found', articles_found, 'articles')
    if articles_skipped > 0:
        print(url, 'skipped', articles_skipped, 'articles')

def process(article: Article.Article):
    print('processing url:', article.url)
    text = article_classification_prompt.format(title=article.title, description=article.description, text=article.text, keywords=', '.join(article.keywords))
    print(text)
    retry = 0
    while True:
        retry += 1
        if retry >= 10:
            print('max retry reached')
            break
        try:
            t = time.time()
            print('sending request to local ggml server')
            # TODO: temperature crashing
            resp = requests.post(LLM_SERVER+'/completion', json={"prompt": text, "temp": "0"}, timeout=1800)
            respText = resp.json()['content']
            print(respText)
            if 'korrupció' in respText:
                print('found corruption', article.title)
                articles.append(article)
            elapsed_time = time.time() - t
            print('done in:', elapsed_time)
            break
        except Exception as e:
            traceback.print_exc()
            print('exception occured, retrying in 10 seconds')
            time.sleep(10)


with open('feed_urls.json') as feed_file:
    feed_urls: [str] = json.load(feed_file)
with open('skip_url_patterns.json') as skip_url_file:
    skip_url_patterns: [str] = json.load(skip_url_file)

articles, seen, article_queue = load_state()
#init_seen()
save_state()
Thread(target=rss_watcher, daemon=True).start()
Thread(target=article_processor, daemon=True).start()
app = Flask(__name__)

@app.route("/")
def article_list_page():
    global articles
    if request.args.get('url'):
        url = request.args.get('url')
        print('url:', url)
        for article in articles:
            if article.url == url:
                print('title:', article.title)
                #ar.add_data(article.text, meta={'url': article.url, 'title': article.title, 'description': article.description, 'date': article.date, 'keywords': article.keywords})
                with open('non_corruption.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow([article.url, article.title, article.description, article.text, article.date, ','.join(article.keywords)])
        articles = [article for article in articles if article.url != url]
    if request.args.get('url_corr'):
        url = request.args.get('url_corr')
        print('url_corr:', url)
        articles = [article for article in articles if article.url != url]
    #TODO: validate input/use templates
    return '\n<hr>\n'.join(['<h3><a href="'+article.url+'">'+article.title+"</a></h3>\n<p>"+article.description+'</p>\n<time>'+article.date+'</time>'+'<a href="/?url_corr='+article.url+'">korrupció</a>'+'<p> </p>'+'<a href="/?url='+article.url+'">nem korrupció</a>' for article in articles])