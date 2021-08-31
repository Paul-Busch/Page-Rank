import requests
from html.parser import HTMLParser
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def crawler(link):    
    r = requests.get(link, verify=False)
    li = []
    #print(r.text)
    
    parser = MyHTMLParser(link, li)
    parser.feed(r.text)
    modified_link = str(link)
    for char in "/\:#.":
        modified_link = modified_link.replace(char,"")
    print(modified_link)

        
    #name = str(link) + ".txt"
    f = open(modified_link, "w+" , encoding="utf8")
    f.write(r.text)
    return(li)
    
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
                            if not values[0] == "#" and ".rss" not in values:
                                if not values[0].isalpha():
                                    values = self.link + values
                                #print(values)
                                self.li.append(values)
        
a = crawler("https://www.math.kit.edu/")
#print(a)
#response = requests.get(a[3], verify = False)
#print(response.status_code)
#print(len(a))