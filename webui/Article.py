import newspaper
import re
from urllib.parse import urlparse

with open('common_descriptions.txt') as f:
    common_descriptions = f.readlines()

with open('common_lines.txt') as f:
    common_lines = f.readlines()

def clear_url(url):
    u = urlparse(url)
    return u.scheme +'://'+ u.netloc + '/' + u.path.replace('www.', '').strip('/')

def do_replacements(text, replacements):
    for pattern, replacement in replacements:
        text = pattern.sub(replacement, text)
    return text

picture_pattern = re.compile(r'Fotó: (\w+\/[^\s]+ [^\s]+|MTI)')
picture_pattern = re.compile(r'Fotó: .*')
quote_pattern = re.compile(r'[”“„]')
dot_pattern = re.compile(r'[…]')
line_pattern = re.compile(r'^\d{4}\. [^\s]+ \d{2}\., [^\s]+, \d{2}\:\d{2} • .*$|(^Szerző: .*$)|(^Címkék: .*$)|(^Kiemelt kép: .*$)')
space_pattern = re.compile(r'  +')
newline_pattern = re.compile(r'\n\n+')
dash_pattern = re.compile(r'\–')
photo_camera_pattern = re.compile(r'photo_camera*')

replacements = [(picture_pattern, ''), (quote_pattern, '"'),
                (dot_pattern, '...'), (line_pattern, ''),
                (space_pattern, ' '), (dash_pattern, '-'),
                (photo_camera_pattern, ''), (newline_pattern, '\n\n')]

class Article:
    def __init__(self, url: str):
        self.url: str = clear_url(url)

        news_article = newspaper.Article(url)
        news_article.download()
        news_article.parse()

        self.title: str = news_article.title
        self.description: str = news_article.meta_description
        self.text: str = news_article.text+'\n'
        self.keywords: [str] = news_article.keywords
        if news_article.publish_date is not None:
            self.date: str = news_article.publish_date.strftime('%Y. %m. %d. %H:%M:%S')
        else:
            self.date: str = ''

        self.text = do_replacements(self.text, replacements)
        self.description = do_replacements(self.description, replacements)
        self.title = do_replacements(self.title, replacements)

        for description in common_descriptions:
            self.description = self.description.replace(description.strip(), '')

        for line in common_lines:
            if line in self.text:
                self.text = self.text.replace('\n'+line, '\n')

        if len(self.description) < 1 and self.text.count('\n') > 1:
            sl = self.text.splitlines()[0]
            self.description = sl[:sl[:400].rfind('.')+1]
            if '.' not in sl[:400]:
                self.description = sl[:400]

        self.text = do_replacements(self.text, replacements).strip()
        self.description = do_replacements(self.description, replacements).strip()
        self.title = do_replacements(self.title, replacements).strip()
        
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def __json__(self):
        return self.__dict__()