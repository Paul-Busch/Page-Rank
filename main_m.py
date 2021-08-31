import merging_file as mf
import concurrent.futures

if __name__ == "__main__":
    t1 = mf.Table("https://www.math.kit.edu")
    table = t1.get_table()
    matr = mf.EvalMatrix(table)
    s = matr.sort_links()

    word = input("Search for: ")
    for link in s.keys():
        if word in link.text:
            print(link)
            

