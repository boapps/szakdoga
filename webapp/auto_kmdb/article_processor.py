import time
import traceback

import requests

from auto_kmdb.Article import Article
from auto_kmdb.db import db

LLM_SERVER = 'http://127.0.0.1:8085'
article_classification_prompt = '''{title}
{description}'''


def article_processor(appcontext):
    appcontext.push()
    while True:
        query = Article.query.filter_by(is_classified=False)
        print(query.count())
        while query.count() > 0:
            process(query.first())
            query.first().is_classified = True
            db.session.commit()
        time.sleep(1*60)


def process(article: Article):
    print('processing url:', article.url)
    text = article_classification_prompt.format(
        title=article.title, description=article.description, text=article.text, keywords=', '.join(article.keywords))
    print(text)
    retry = 0
    while True:
        retry += 1
        if retry >= 10:
            print('max retry reached')
            break
        try:
            t = time.time()
            print('sending request to local bert server')
            resp = requests.post(LLM_SERVER+'/classify',
                                 json={"text": text}, timeout=1800)
            respText = resp.json()['class']
            print(respText)
            if respText == 'corruption':
                print('found corruption', article.title)
                db.session.commit()
                article.is_corruption = True
            elapsed_time = time.time() - t
            print('done in:', elapsed_time)
            break
        except Exception:
            traceback.print_exc()
            print('exception occured, retrying in 10 seconds')
            time.sleep(10)
