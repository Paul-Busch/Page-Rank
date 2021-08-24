import table as t
import numpy as np

class EvalMatrix():

    def __init__(self, table):
        self.table = table
        
    def calculate_weight(self, key_x, key_y):
        # key_x is the html_link on the horizontal in the A matrix (x-axis)
        # key_y is the html_link on the vertical in the A matrix (y-axis)

        # count outgoing links:
        L = len(self.table[key_x])
        
        # calculate x:
        # the counter represents the number of all outgoing links 
        counter = 0
        for link in self.table[key_x]:
            if link == key_y:
                counter += 1
         
        if counter == 0:
            return 0
        else:
            return counter/L           

    def build_matrix_A(self):
        sorted_keys = sorted(self.table)

        # initialize A as a zero matrix
        A = np.zeros((len(self.table), len(self.table)))
        counter_x = 0
        #for key_x in self.table:
        for key_x in sorted_keys: 
            counter_y = 0
            
            #for key_y in self.table:
            for key_y in sorted_keys:
                A[counter_y,counter_x] = self.calculate_weight(key_x, key_y)
                #print("counter_x, counter_y = ", counter_x, counter_y)
                counter_y += 1

            counter_x += 1
        print("A after the calc: ",A)

            # calculate weight for every key

        #calculate the weights for every key in table
        return A
    
    def calculate_matrix_M(self):
        pass






table = t.Table("1").get_table()

#EvalMatrix(table).build_matrix_A()


test = "test2"

# test for calculate_weight()
if test == "test1":
    x21 = EvalMatrix(table).calculate_weight("2", "1")
    x62 = EvalMatrix(table).calculate_weight("6", "2")
    print("x21 = ", x21, "x12 = ", x62)

# test for build_matrix_a()
if test == "test2":
    A = EvalMatrix(table).build_matrix_A()
    #print(A)




