from html.parser import HTMLParser
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = requests.get('https://www.math.kit.edu'.format(4980), verify= False)
print(r.status_code)

if r.status_code == 200:
    #r.encoding = r.apparent_encoding
    print(r.text)