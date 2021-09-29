# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:49:30 2021

@author: sontr
"""

import requests
from html.parser import HTMLParser
import urllib3
import time
import numpy as np
import json

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

        # first coloum in the dict is the link "www.math.kit.edu"
        init_table[self.html_link] = self.html_list

        k = 0
        #for link in crawler(starting_point):
        for link in self.html_list:
            if k <= 15:
                try:
                    """
                    if math.kit.edu not in link:
                        throw exeption
                    """
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

class EvalMatrix():

    def __init__(self, table):
        self.table = table
        
    def calculate_weight(self, key_x, key_y):
        # key_x is the html_link on the horizontal in the A matrix (x-axis)
        # key_y is the html_link on the vertical in the A matrix (y-axis)

        # count outgoing links:
        L = len(self.table[key_x])
        
        # calculate x:
        # the counter represents the number of all outgoing links 
        counter = 0
        for link in self.table[key_x]:
            if link == key_y:
                counter += 1
         
        if counter == 0:
            return 0
        else:
            return counter/L           

    def build_matrix_A(self):
        sorted_keys = sorted(self.table)

        # initialize A as a zero matrix
        A = np.zeros((len(self.table), len(self.table)))
        counter_x = 0
        for key_x in sorted_keys: 
            counter_y = 0
            for key_y in sorted_keys:
                A[counter_y,counter_x] = self.calculate_weight(key_x, key_y)
                counter_y += 1
            counter_x += 1

            # calculate weight for every key

        #calculate the weights for every key in table
        return A
    
    def calculate_matrix_M(self):
        B = np.ones((len(self.table), len(self.table)))
        M = (1 - 0.15) * self.build_matrix_A() + (0.15 / len(self.table)) * B
        return M 

    def calculate_vector_iteration(self):
        M = self.calculate_matrix_M()
        # start with x_0
        x_k = np.ones(len(self.table))
        x_k1 = np.dot(M, x_k)
        while np.max(x_k - x_k1) > 0.0001:
            x_k = x_k1
            x_k1 = np.dot(M, x_k)
        # if x_k - x_k1 is small return x_k1
        return x_k1

    def sort_links(self):
        d = {}
        x = self.calculate_vector_iteration()
        links = list(self.table.keys())
        for l in range(0, len(x)):
            d[links[l]] = x[l] 
        d2 = {key: value for key, value in sorted(d.items(), reverse = True,  key=lambda item: item[1])}
        print(d2)
        return d2

    def save_json(self):
        dic = self.sort_links()
        with open("sorted.json", "w") as outfile:
            json.dump(dic, outfile)

    def save(self):
        with open ('sorted.txt', 'w') as sl:
            sl.write('{0}\n'.format(', '.join(str(n) for n in self.sort_links())))




table = Table("https://www.math.kit.edu/").get_table()


#s = EvalMatrix(table)
#s.save()

test = ""

# test for calculate_weight()
if test == "test1":
    x21 = EvalMatrix(table).calculate_weight("2", "1")
    x62 = EvalMatrix(table).calculate_weight("6", "2")
    print("x21 = ", x21, "x12 = ", x62)

# test for build_matrix_a()
if test == "test2":
    A = EvalMatrix(table).build_matrix_A()
    #print(A)

# test for calculate_vector_iteration()
if test == "test3":
    x = EvalMatrix(table).calculate_vector_iteration()
    print("Eigenvektor:", x)

# test for sort_links
if test == "test4":
    d = EvalMatrix(table).sort_links()
    print("sorted:", d)