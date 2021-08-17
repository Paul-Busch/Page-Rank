import requests
from html.parser import HTMLParser

r = requests.get("https://www.math.kit.edu", verify=False)
#print(r.text)


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name,values in attrs:
                if name == "href":
                    print(values)
        



parser = MyHTMLParser()
parser.feed(r.text)