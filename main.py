import merging_file as mf


t1 = mf.Table("https://www.math.kit.edu")
table = t1.get_table()
matr = mf.EvalMatrix(table)
matr.sort_links()