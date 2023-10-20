import time
import traceback

import requests

from auto_kmdb.Article import Article
from auto_kmdb.db import db

CLASSIFICATION_SERVER = 'http://127.0.0.1:8085'
KEYWORD_GENERATION_SERVER = 'http://127.0.0.1:8086'
article_classification_prompt = '''{title}
{description}'''
keyword_generation_prompt = '''[címkék generálása]
{title}

{description}

{text}

cimkék: {keywords}

###

korrupciós címkék:'''


def article_processor(appcontext):
    appcontext.push()
    while True:
        query = Article.query.filter_by(is_classified=False)
        while query.count() > 0:
            article = query.first()
            process(article, do_classification)
            db.session.commit()
            if article.is_classified_corruption:
                process(article, do_keyword_generation)
            db.session.commit()
        time.sleep(1*60)


def do_classification(article: Article):
    text = article_classification_prompt.format(title=article.title,
            description=article.description, text=article.text,
            keywords=', '.join(article.keywords))
    resp = requests.post(CLASSIFICATION_SERVER+'/classify',
                                 json={"text": text}, timeout=1800)
    respText = resp.json()['class']
    print(respText)
    if respText == 'corruption':
        print('found corruption', article.title)
        article.is_classified_corruption = True
    article.is_classified = True


def do_keyword_generation(article: Article):
    text = keyword_generation_prompt.format(title=article.title,
            description=article.description, text=article.text,
            keywords=', '.join(article.keywords))

    resp = requests.post(KEYWORD_GENERATION_SERVER+'/completion',
                                 json={"prompt": text}, timeout=1800)
    respText = resp.json()['content'].strip()
    print(respText)
    article.tags = respText


def process(article: Article, f):
    print('processing url:', article.url)
    retry = 0
    while True:
        retry += 1
        if retry >= 10:
            print('max retry reached')
            break
        try:
            t = time.time()
            print('sending request to local server')
            f(article)
            elapsed_time = time.time() - t
            print('done in:', elapsed_time)
            break
        except Exception:
            traceback.print_exc()
            print('exception occured, retrying in 10 seconds')
            time.sleep(10)
