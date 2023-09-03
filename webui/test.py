import unittest
from Article import Article

class MyTest(unittest.TestCase):
    def test(self):
        article = Article('https://telex.hu/belfold/2023/08/08/pesty-laszlo-ner-lolo-egybites-kessel-villaval-enni-nem-tudo')
        print(article.title)
        print(article.description)
        print(article.text)
        print()

if __name__ == '__main__':
    unittest.main()