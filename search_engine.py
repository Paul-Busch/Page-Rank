import json 
from concurrent import futures

class SearchEngine():
    '''
    params: word
    returns: approximatly 10 words for each time the word is found on a website
    '''
    
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
        '''
        params: none
        returns: prints the link, and context for word
        '''
        dictionary_final = self.paralleled()

        for link in dictionary_final:
            if dictionary_final[link]:
                print(link , "hat die Wichtigkeit: " , dictionary_final[link][0] ,'\n', dictionary_final[link][1], '\n')


    def get_list_of_lines(self, data):
        '''
        params: data --> .txt data
        returns: lst_of_lines --> list
        This functions returns a list that includes all lines that include the relevant word
        '''
        lst_of_lines = []
        with open(data, "r") as f:
            text = f.read()
            f_liste = text.split(" ")
            for element in range(0, len(f_liste)):
                if self.word in f_liste[element]:
                    if element < 5:
                        lst_of_lines.append(' '.join([f_liste[x] for x in range(0, element+5)]))
                    elif (len(f_liste) - element) < 5:
                        lst_of_lines.append(' '.join([f_liste[x] for x in range(element-5, len(f_liste))]))
                    else:
                        lst_of_lines.append(' '.join([f_liste[x] for x in range(element-5, element+5)]))
        return lst_of_lines



    def get_dict_of_lines(self, link, dict_full_info):
        '''
        params: dictionary with importance of links and actual link
        returns: importance of link and context for link (list_of_lines) as list
        '''
        doc = self.get_document(link)
        list_of_lines = self.get_list_of_lines(doc)
        if list_of_lines:
            return [dict_full_info[link], list_of_lines] #self.dict_full_info[key] greif auf die Wichtigkeit zu
   
    def paralleled(self):
        '''
        for each link calls get_dict_of_lines to make final dictionary. 
        params: none
        returns: dictionary final: a dictionary that contains all relevant links with the importance and context
        '''
        dict_full_info = self.get_dict()
        dictionary_final = {}
        for key in dict_full_info:
            dictionary_final[key] = self.get_dict_of_lines(key, dict_full_info)
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




