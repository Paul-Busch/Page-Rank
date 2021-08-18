

class MyHtmlParser():

    lst1 = ["2","3","4","5","6"]
    lst2 = ["3","4","5"]
    lst3 = ["1", "6"]
    lst4 = ["1", "3"]
    lst5 = ["1", "6"]
    lst6 = ["2", "4"]

    def __init__(self, html_link): 
        self.html_link = html_link 
        

    def handleStartTag(self):
        if self.html_link == "1":
            return MyHtmlParser.lst1
        elif self.html_link == "2":
            return MyHtmlParser.lst2
        elif self.html_link == "3":
            return MyHtmlParser.lst3
        elif self.html_link == "4":
            return MyHtmlParser.lst4
        elif self.html_link == "5":
            return MyHtmlParser.lst5
        elif self.html_link == "6":
            return MyHtmlParser.lst6

class Table(): 

    def __init__(self, html_link):
        self.html_link = html_link

    def find_missing_keys(self, table):
        #initialize empty list that will contain the missing keys
        lst_keys = []
        for key in self.table:
            for link in table[str(key)]:
                if not link in table:
                    lst_keys.append(link)
        return lst_keys


    def create_init_table(self):
        init_table = dict()
        starting_point = self.html_link

        for link in MyHtmlParser(starting_point).handleStartTag():     
        # hier werden doppelte keys überschrieben
           #create initial table where keys are from the list of the given html_link
            init_table[link] = MyHtmlParser(link).handleStartTag()
        
        #print(init_table)
        return init_table
    
    def update_table(self):
        table = self.create_init_table()
        print(table)
   





        
t = Table("1")
table1 = t.update_table()

