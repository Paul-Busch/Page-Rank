import requests
from html.parser import HTMLParser

r = requests.get("https://www.math.kit.edu", verify=False)
#print(r.text)


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", 'href')
        print(self.get_starttag_text())
        



parser = MyHTMLParser()
parser.feed(r.text)