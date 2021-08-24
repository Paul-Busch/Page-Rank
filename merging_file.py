import requests
from html.parser import HTMLParser
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def crawler(link):    
    r = requests.get(link, verify=False)
    li = []
    #print(r.text)
    
    parser = MyHTMLParser(link, li)
    parser.feed(r.text)
    #print(li)
    return li

    
class MyHTMLParser(HTMLParser):
    def __init__(self, link, li):
        super().__init__()
        self.link = link
        self.li = li

    def handle_starttag(self, tag="a", attrs=""):
        li = []
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
    

class Table(): 

    def __init__(self, html_link):
        self.html_link = html_link
        self.html_list = crawler(self.html_link)

    def find_missing_keys(self, table):
        # this function searches in the lists (values) of every key for links that are not yet a key
        # we want every link that is in a list (value) should also be a key  
        # initialize empty list that will contain the missing keys
        lst_missing_keys = []
        for key in table:
            for link in table[str(key)]:
                if not link in table:
                    # don't save duplicates in the lst_missing_keys
                    lst_missing_keys.append(link) if link not in lst_missing_keys else None
        
        return lst_missing_keys

    def create_init_table(self):
        # returns an initale dictionary (table):
        # keys are all outgoing links of the html_link (starting_link)
        # values are lists with all outgoing links of the certain key
        # that means the function creates a table with depth 1 
        init_table = dict()
        starting_point = self.html_link
        #TODO: hier muss starting point auch in den init table eingebaut werden
        k = 0
        #for link in crawler(starting_point):
        for link in self.html_list:
            if k <= 15:
                try:
                # hier werden doppelte keys überschrieben
                #create initial table where keys are from the list of the given html_link
                    init_table[link] = crawler(link)
                    k += 1
                    print("alles okay", link)
                except:
                    self.html_list.remove(link)
                    print("dieser link funktioniert nicht", link)
                    continue
            else:
                break
            
        print("Done")
        return init_table

    def update_table(self, table):
        # updates a given table
    
        #table = self.create_init_table()
        #print("given table is:", table)
        # find missing keys
        missing_keys = self.find_missing_keys(table)

        #print("missing keys are:", missing_keys)
        # missing keys are added to the table
        k = 0
        for link in missing_keys:
            if k <= 15:
                try:
                    table[link] = crawler(link)
                    k += 1
                except:
                    continue
            else:
                break

    def get_table(self, depth=3):
        # returns table with certain depth (Suchtiefe)
        table = self.create_init_table()
        i = 1
        print("ich bin hier 3")
        for i in range(1,depth):
            print(i)
            self.update_table(table)
            print("updated table in der Schleife:", table)
        return table

#print(crawler("https://www.math.kit.edu/"))

t = Table("https://www.math.kit.edu/")
#t.create_init_table()
print("ich bin hier 1")
dict_1 = t.get_table()
print("fertige Tabelle:", dict_1)
print("ich bin hier 2")