# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:42:02 2021

@author: sontr
"""
from concurrent import futures

#in Konstruktor: self.dictionary_final = {}
def get_dict_of_lines(self, link):
    #gegeben: Dictionary mit Information wo Sachen stehen
    #List mit Links sortiert
    #dic_lines = {"link": [lines]}
    #list_sorted ist die Liste der sortierten Links
    #TODO: get sorted dictionary of links called d2
    doc = get_document(key)
    list_of_lines = get_list_of_lines(doc) #Hab das word weggemacht, lieber self.word verweden
    if list_of_lines:
        self.dictionary_final[key] = [d2[key], list_of_lines]
        
        

def paralleled(self):
    with futures.ProcessPoolExecutor(max_workers=4) as ex:
        for key in d2:
            ex.submit(get_dict_of_lines, key)
    if ex.done():
        self.dictionary_final = {k: v for k, v in sorted(self.dictionary_final.items(), key=lambda item: item[1])}
        