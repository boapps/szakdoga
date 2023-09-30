import newspaper
import re
from urllib.parse import urlparse

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def clear_url(url):
    """
    Clears the URL by removing .www and any trailing slashes.

    Args:
        url (str): The URL to be cleared.

    Returns:
        str: The cleared URL.
    """
    u = urlparse(url)
    return u.scheme +'://'+ u.netloc + '/' + u.path.replace('www.', '').strip('/')

def do_replacements(text, replacements):
    """
    Replace all occurrences of patterns in a string with their corresponding replacements.

    Parameters:
        text (str): The input string.
        replacements (dict): A dictionary of patterns and their corresponding replacements.

    Returns:
        str: The output string with all occurrences of patterns replaced.
    """
    for pattern, replacement in replacements:
        text = pattern.sub(replacement, text)
    return text

common_descriptions = read_file('common_descriptions.txt')
common_lines = read_file('common_lines.txt')

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

        self.news_article = newspaper.Article(self.url)
        self.download()
        self.parse()
        
        self.prepare_title()
        self.prepare_text()
        self.prepare_description()
        self.prepare_keywords()
        self.prepare_date()

        self.text = do_replacements(self.text, replacements).strip()
        self.description = do_replacements(self.description, replacements).strip()
        self.title = do_replacements(self.title, replacements).strip()

    def download(self):
        self.news_article.download()

    def parse(self):
        self.news_article.parse()

    def prepare_title(self):
        self.title: str = self.news_article.title
        self.title = do_replacements(self.title, replacements)

    def prepare_text(self):
        self.text: str = self.news_article.text+'\n'
        self.text = do_replacements(self.text, replacements)
        for line in common_lines:
            if line in self.text:
                self.text = self.text.replace('\n'+line, '\n')

    def prepare_description(self):
        self.description = self.news_article.meta_description
        self.description = do_replacements(self.description, replacements)

        for description in common_descriptions:
            self.description = self.description.replace(description.strip(), '')

        if len(self.description) < 1 and self.text.count('\n') > 1:
            sl = self.text.splitlines()[0]
            self.description = sl[:sl[:400].rfind('.')+1]
            if '.' not in sl[:400]:
                self.description = sl[:400]

    def prepare_keywords(self):
        self.keywords = self.news_article.keywords

    def prepare_date(self):
        self.date = self.news_article.publish_date
        if self.date is not None:
            self.date = self.date.strftime('%Y. %m. %d. %H:%M:%S')
        else:
            self.date = ''

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['news_article']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def __json__(self):
        return self.__dict__()