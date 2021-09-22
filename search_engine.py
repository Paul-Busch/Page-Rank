import json 

class SearchEngine():
    
    def __init__(self, word):
        self.word = word

    def get_document(self, link):
        # gibt das entsprechende dokument (path) für den jeweiligen link zurück
        # konvertiere modified link
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
        pass

    """def print_output(word, data, link):
        search_for_word(word, data, link)
        print(link,"\n",line)"""


    def get_list_of_lines(self, data, word):
        '''
        params: data --> html text, word --> string
        returns: lst_of_lines --> list
        This functions returns a list that includes all lines that include the relevant word
        '''
        # TODO: Paul
        lst_of_lines = []
        with open(data) as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    lst_of_lines.append(line)
        return lst_of_lines

    def get_dict_of_lines(self):
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


                
