from html.parser import HTMLParser
import requests
r = requests.get(
    'https://www.math.kit.edu', verify= False)

if r.status_code == 200:
    #r.encoding
	print(r.text)


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        #if tag == "a":
           # Check the list of defined attributes.
        for name, value in attrs:
            print("called")
            # If href is defined, print it.
            if name == "href":
                print (name, "=", value)
                print("called")


parser = MyHTMLParser()
parser.feed('https://www.math.kit.edu')