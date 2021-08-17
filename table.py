lst1 = ["2","3","4","5","6"]
lst2 = ["3","4","5"]
lst3 = ["1", "6"]
lst4 = ["1", "3"]
lst5 = ["1", "6"]
lst6 = ["2", "4"]

class MyHtmlParser():
    def __init__(self): pass

    def handleStartTag(html_link):
        if html_link == "1":
            return lst1
        elif html_link == "2":
            return lst2
        elif html_link == "3":
            return lst3
        elif html_link == "4":
            return lst4
        elif html_link == "5":
            return lst5
        elif html_link == "6":
            return lst6

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

        for link in MyHtmlParser.handleStartTag(starting_point):     
        # hier werden doppelte keys überschrieben
           #create initial table where keys are from the list of the given html_link
            init_table[link] = MyHtmlParser.handleStartTag(link)
        
        print(table)
        return init_table
        
   





        

table1 = Table("1").get_table()

