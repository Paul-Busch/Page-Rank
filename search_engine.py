
class SearchEngine():
    
    def __init__(self, word):
        self.word = word

    def get_document(self):
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

    def get_dict_of_lines(self):
        # TODO: Sontraud
        # input alle html links bzw. deren dokumente

        # loop über alle html links bzw. deren und schaut ob in dem document 
        # parallelisieren
        # return dic_lines = {"link": lines)}
        pass



                

