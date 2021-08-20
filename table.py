
class MyHTMLParser_2():

    lst1 = ["2","3","4","5","6"]
    lst2 = ["3","4","5"]
    lst3 = ["1", "6"]
    lst4 = ["1", "3"]
    lst5 = ["1", "6"]
    lst6 = ["2", "4"]

    def __init__(self, html_link): 
        self.html_link = html_link 
        

    def handle_starttag(self):
        if self.html_link == "1":
            return MyHTMLParser_2.lst1
        elif self.html_link == "2":
            return MyHTMLParser_2.lst2
        elif self.html_link == "3":
            return MyHTMLParser_2.lst3
        elif self.html_link == "4":
            return MyHTMLParser_2.lst4
        elif self.html_link == "5":
            return MyHTMLParser_2.lst5
        elif self.html_link == "6":
            return MyHTMLParser_2.lst6

class Table(): 

    def __init__(self, html_link):
        self.html_link = html_link

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

        for link in MyHTMLParser_2(starting_point).handle_starttag():     
        # hier werden doppelte keys überschrieben
           #create initial table where keys are from the list of the given html_link
            init_table[link] = MyHTMLParser_2(link).handle_starttag()
        
        #print(init_table)
        return init_table
    
    def update_table(self, table):
        # updates a given table
    
        #table = self.create_init_table()
        print("given table is:", table)
        # find missing keys
        missing_keys = self.find_missing_keys(table)

        print("missing keys are:", missing_keys)
        # missing keys are added to the table
        for link in missing_keys:
            table[link] = MyHTMLParser_2(link).handle_starttag()

    def get_table(self, depth=3):
        # returns table with certain depth (Suchtiefe)
        table = self.create_init_table()
        i = 1
        for i in range(1,depth):
            self.update_table(table)
            #print("updated table in der Schleife:", table)
        return table






        
t = Table("1")
table1 = t.get_table()
