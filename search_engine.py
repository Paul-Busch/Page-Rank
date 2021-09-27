import json 
from concurrent import futures

class SearchEngine():
    
    def __init__(self, word):
        self.word = word
        # self.dictionary_final = {}

    def get_document(self, link):
        '''
        params: link
        returns: document corresponding to link
        '''
        modified_link = str(link)
        for char in "/\:#.":
            modified_link = modified_link.replace(char,"")
        return '/Users/Paul/Documents/Uni/Master 5. Semester/Einführung in Python/Page-Rank/html_data/'+modified_link+'.txt'
            
    
    def get_dict(self):
        '''
        params: none
        returns: dictonary including every outgoing/ ingoing links as keys and their rank as values in terms of the eigenvalue
        '''
        with open('sorted.json') as json_file:
            sorted_dict = json.load(json_file)
            #print(sorted_dict)
        return sorted_dict
    
    def print_output(self):
        #TODO: all 
        # loop über dict_values und schaue ob der jeweilige link keine leere liste in dic_lines aufweist 
        # liste mit relevanten html links -> sortiert 
        # unter jedem link (entweder fett oder eingerückt) die relevanten zeilen ausgeben
        dictionary_final = self.paralleled()

        for link in dictionary_final:
            if dictionary_final[link]:
                print(link,'\n', dictionary_final[link][1])

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
        #print(lst_of_lines)
        return lst_of_lines

    #TODO Sontraud: Funktion testen --> dict_full_info ist instanz aus anderer Klasse
    def get_dict_of_lines(self, link, dict_full_info):
        doc = self.get_document(link)
        #print(doc)
        list_of_lines = self.get_list_of_lines(doc)
        #print(list_of_lines)
        if list_of_lines:
            return [dict_full_info[link], list_of_lines] #self.dict_full_info[key] greif auf die Wichtigkeit zu 
   
    #TODO Sontraud: Funktion testen --> dict_full_info ist instanz aus anderer Klasse
    '''def paralleled(self):
        dict_full_info = self.get_dict()
        with futures.ThreadPoolExecutor() as ex:
            for key in dict_full_info:
                ex.submit(self.get_dict_of_lines, key, dict_full_info)
        self.dictionary_final = {k: v for k, v in sorted(self.dictionary_final.items(), key=lambda item: item[1])}
        return self.dictionary_final'''
    
    def paralleled(self):
        dict_full_info = self.get_dict()
        dictionary_final = {}
        #with futures.ThreadPoolExecutor() as ex:
        for key in dict_full_info:
            dictionary_final[key] = self.get_dict_of_lines(key, dict_full_info)
            #dictionary_final[key] = zwvar.result()
        """for link in dictionary_final:
            try:
                print(dictionary_final[link][0])
            except:
                pass"""
        """try:
            dictionary_final = {k: v for k, v in sorted(dictionary_final.items(), key=lambda item: item[0])}
        except:
            print("There has been an error")
        finally:"""
        return dictionary_final

    def print_dic(self):
        dic = self.paralleled()
        print(dic)
        return

Test1 = False
Test2 = False

if Test1:
    t1 = SearchEngine("Hallo")
    
    lst = t1.get_list_of_lines("Page-Rank\test.txt")
    print(lst)

if Test2:
    printout = SearchEngine("Mathe").get_list_of_lines("sorted.txt")
    print(printout)

#search_engine = SearchEngine("KIT")


#search_engine.print_output()



