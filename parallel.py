def get_dict_of_lines(self, link, dict_full_info):
        doc = self.get_document(link)
        list_of_lines = self.get_list_of_lines(doc)
        if list_of_lines:
            return [dict_full_info[link], list_of_lines] #self.dict_full_info[key] greif auf die Wichtigkeit zu
   
        """def paralleled(self):
        dict_full_info = self.get_dict()
        with futures.ThreadPoolExecutor() as ex:
            for key in dict_full_info:
                ex.submit(self.get_dict_of_lines, key, dict_full_info)
        self.dictionary_final = {k: v for k, v in sorted(self.dictionary_final.items(), key=lambda item: item[1])}
        

        try:
            self.dictionary_final = {k: v for k, v in sorted(self.dictionary_final.items(), key=lambda item: item[0])}
        except:
            print("There has been an error")
        finally:
            return self.dictionary_final"""
    
def paralleled(self):
    dict_full_info = self.get_dict()
    dictionary_final = {}
    for key in dict_full_info:
        dictionary_final[key] = self.get_dict_of_lines(key, dict_full_info)
        #dictionary_final[key] = zwvar.result()
    #for link in dictionary_final:
        #try:
        #    print(dictionary_final[link][0])
        #except:
        #    pass
    """try:
        dictionary_final = {k: v for k, v in sorted(dictionary_final.items(), key=lambda item: item[0])}
    except:
        print("There has been an error")
    finally:"""
    return dictionary_final