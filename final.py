# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:44:19 2021

@author: sontr
"""

from concurrent import futures


class SearchEngine():
    
    def __init__(self, word):
        self.word = word
        self.dictionary_final = {}
        self.d2 = get_dict()

    def get_document(self, link):
        # TODO: Madlena
        # gibt das entsprechende dokument (path) für den jeweiligen link zurück
        # konvertiere modified link
        pass
    
    def get_dict(self):
        # TODO: Paul
        #json to dict
        pass
    
    def print_output(self):
        #TODO: all 
        # loop über dict_values und schaue ob der jeweilige link keine leere liste in dic_lines aufweist 
        # liste mit relevanten html links -> sortiert 
        # unter jedem link (entweder fett oder eingerückt) die relevanten zeilen ausgeben
        pass

    """def print_output(word, data, link):
        search_for_word(word, data, link)
        print(link,"\n",line)"""


    def get_list_of_lines(self,data, word):
        # TODO: Paul
        # gibt eine liste der relevanten zeilen zurück
        pass 

        """with open(data) as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    print(line)
                    return line"""

    def get_dict_of_lines(self, link):
    #gegeben: Dictionary mit Information wo Sachen stehen
    #List mit Links sortiert
    #dic_lines = {"link": [lines]}
    #list_sorted ist die Liste der sortierten Links
    #TODO: get sorted dictionary of links called d2
        doc = get_document(link)
        list_of_lines = get_list_of_lines(doc) #Hab das word weggemacht, lieber self.word verweden
        if list_of_lines:
            self.dictionary_final[key] = [self.d2[key], list_of_lines] #self.d2[key] greif auf die Wichtigkeit zu
        
        

    def paralleled(self):
        with futures.ProcessPoolExecutor() as ex:
            for key in self.d2:
                ex.submit(get_dict_of_lines, key)
            if ex.done():
                self.dictionary_final = {k: v for k, v in sorted(self.dictionary_final.items(), key=lambda item: item[1])}
                return self.dictionary_final



                

