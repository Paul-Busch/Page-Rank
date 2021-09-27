import json 
from concurrent import futures

class SearchEngine():
    
    def __init__(self, word):
        self.word = word
        self.dictionary_final = {}

    def get_document(self, link):
        '''
        params: link
        returns: document corresponding to link
        '''
        modified_link = str(link)
        for char in "/\:#.":
            modified_link = modified_link.replace(char,"")
        with open (modified_link, "w+" , encoding="utf8") as link_text:
            return link_text
    
    def get_dict(self):
        '''
        params: none
        returns: dictonary including every outgoing/ ingoing links as keys and their rank as values in terms of the eigenvalue
        '''
        with open('sorted.json') as json_file:
            sorted_dict = json.load(json_file)
            print(sorted_dict)
        return sorted_dict
    
    def print_output(self):
        #TODO: all 
        # loop über dict_values und schaue ob der jeweilige link keine leere liste in dic_lines aufweist 
        # liste mit relevanten html links -> sortiert 
        # unter jedem link (entweder fett oder eingerückt) die relevanten zeilen ausgeben
        self.paralleled()
        for link in self.dictionary_final:
            #if paralled().value()[1] =! none:
            print(link, self.dictionary_final[link][1])

    """def print_output(word, data, link):
        search_for_word(word, data, link)
        print(link,"\n",line)"""

    def get_list_of_lines(self, data):
        '''
        params: data --> .txt data
        returns: lst_of_lines --> list
        This functions returns a list that includes all lines that include the relevant word
        '''
        # TODO: Paul
        lst_of_lines = []
        with open(data) as f:
            lines = f.readlines()
            for line in lines:
                if self.word in line:
                    lst_of_lines.append(line)
        return lst_of_lines

    #TODO Sontraud: Funktion testen --> d2 ist instanz aus anderer Klasse
    def get_dict_of_lines(self, link, d2):
        doc = self.get_document(link)
        list_of_lines = self.get_list_of_lines(doc)
        if list_of_lines:
            self.dictionary_final[link] = [self.d2[link], list_of_lines] #self.d2[key] greif auf die Wichtigkeit zu 
   
    #TODO Sontraud: Funktion testen --> d2 ist instanz aus anderer Klasse
    def paralleled(self):
        d2 = self.get_dict()
        with futures.ProcessPoolExecutor() as ex:
            for key in d2:
                ex.submit(self.get_dict_of_lines, key, d2)
            if ex.done():
                self.dictionary_final = {k: v for k, v in sorted(self.dictionary_final.items(), key=lambda item: item[1])}
                #return self.dictionary_final



Test1 = True
Test2 = False

if Test1:
    t1 = SearchEngine("Hallo")
    
    lst = t1.get_list_of_lines("Page-Rank\test.txt")
    print(lst)

"""if Test2:
    printout = SearchEngine("Mathe").get_list_of_lines("sorted.txt")
    print(printout)"""


                
