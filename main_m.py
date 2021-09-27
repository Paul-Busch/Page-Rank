#import merging_file as mf
#import concurrent.futures
import search_engine as se

if __name__ == "__main__":
    """t1 = mf.Table("https://www.math.kit.edu")
    table = t1.get_table()
    matr = mf.EvalMatrix(table)
    s = matr.sort_links()"""

    word = str(input("Search for: "))
    final_search = se.SearchEngine(word)
    final_search.print_output()

    
            

