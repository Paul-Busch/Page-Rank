import requests
from html.parser import HTMLParser
import numpy as np

def crawler(link):    
    r = requests.get(link, verify=False)
    li = []
    #print(r.text)
    
    parser = MyHTMLParser(link, li)
    parser.feed(r.text)
    print(li)
    return li
    
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

class Call(MyHTMLParser):
    def __init__(self):
        super().__init__()
        self.lst = []
        self.v = 0
    
    def s(self, b = False):
        self.s = True
        return b 

    def call(self, link = "https://www.math.kit.edu"):
        lst1 = self.crawler(link)
        print(lst1)
        for x in lst1:
            if x.s():
                return
            else:
                x.index = self.v
                self.lst[self.v][0] = x
                self.lst[link.index][self.v] += 1
                self.v += 1
                self.call(x)
        print(self.lst)


        
            

        
