import requests
from html.parser import HTMLParser

def crawler(link):    
    r = requests.get(link, verify=False)
    li = []
    #print(r.text)
    
    parser = MyHTMLParser(link, li)
    parser.feed(r.text)
    print(li)
    
class MyHTMLParser(HTMLParser):
    def __init__(self, link, li):
        super().__init__()
        self.link = link
        self.li = li
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name,values in attrs:
                if name == "href":
                    if not "@" in values:
                        isALetter = False
                        for l in values:
                            isALetter = isALetter or l.isalpha()
                        if isALetter:
                            if values[0] is not "#" and ".rss" not in values:
                                if not values[0].isalpha():
                                    values = self.link + values
                                print(values)
                                self.li.append(values)

crawler("https://www.math.kit.edu/")