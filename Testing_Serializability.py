import numpy as np
print("\tHow does my algo work:\nA numpy 2d zero array will be created (representing a table like structure)")
print("then it will take user input and store the operation , element as a single list element like [['R', 'X']]which is Read(X)")
print("then it will search for read or write in the 2d array since there are zeros also")
print("and if read is encountered it will reform a matrix which will not consist the same and all above rows and the same column")
print("then it will search for write and the same element eg.if read(X) was encountered then search for Write(X) in inner matrix")
print("and if the search is successful then it will append the element and its location in a list named conflicting")
print("then by using the position we will determine if the cycle is present or not and also the indegree of each transaction using the position of conflicting pair.")

# creating pre defined list
'''l1 = [0 ,0, ['R', 'Y']]
l2 = [0, 0, ['R', 'Z']]
l3 = [['R', 'x'],0, 0]
l4 = [['w', 'Y'], 0, 0]
l5 = [0 ,0,['W', 'Y']]
l6 = [0, 0, ['W', 'Z']]
l7 = [0, ['R', 'Z'] , 0]
l8 = [['R', 'Y'], 0, 0]
l9 = [['W', 'Y'], 0, 0]
l10 = [0 ,['R', 'Y'], 0]
l11 = [0 ,['W', 'Y'], 0]
l12 = [0 ,['R', 'x'], 0]
l13 = [0 ,['W', 'X'], 0]
list = []
list.append(l1)
list.append(l2)
list.append(l3)
list.append(l4)
list.append(l5)
list.append(l6)
list.append(l7)
list.append(l8)
list.append(l9)
list.append(l10)
list.append(l11)
list.append(l12)
list.append(l13)

# convert list to numpy array
matrix = np.array(list, dtype=object)'''
    
print("\nFirst input the number of total time in schedule")
print("Then the number of Transaction in which you want to insert the specific element")
print("Then the operation (R for Read or W for Write)")
print("Then the element on which the operation has to be done (X, Y, Z)")
print("Note : please enter operation and element in only caps (R, W, X, Y, Z).\n")
# code for user input
time = int(input("Time: "))

matrix = np.zeros((time,3), dtype=object)
for i in range(time):
    
    print("\nFor Time ", i+1)
    transaction = int(input("Transaction (1/2/3): "))
    operation = str(input("Operation (R/W): "))
    element = str(input("Element (X/Y/Z): "))
    matrix[i, transaction-1] = [operation, element]

conflicting = []
# full matrix pass
# for user input
for row in range(time):    
#for row in range(13):
    for col in range(3):
        # select only operations i.e non zero
        if matrix[row, col] != 0:
            temp = matrix[row, col]
            # splitting operation and on expression
            temp_o = temp[0]
            temp_e = temp[1]
            # if encountered read then it will check for write in inner matrix
            if 'R' in temp:
                # copy original matrix so that we can select rows and columns to search into for further condition
                matrix_copy = matrix
                # only taking below rows in inner matrix
                matrix_copy2 = matrix[row+1:,:]
                # delete the column in which read is encountered
                matrix_copy2 = np.delete(matrix_copy2, col, axis=1)
                row_in, col_in = matrix_copy2.shape
                # only forward and below matrix pass
                for r in range(row_in):
                    for c in range(col_in):
                        #if matrix_copy2[r, c] != 0 and counter==0:
                        if matrix_copy2[r, c] != 0:
                            temp_in = matrix_copy2[r, c]
                            temp_in_o = temp_in[0]
                            temp_in_e = temp_in[1]
                            # checking for write in inner matrix and X==X or Y==Y or Z==Z
                            if temp_in_o =='W' and (temp_e==temp_in_e):
                                # since the inner matrix has different column and row indexes converting c, r to original matrix col, row
                                if col==0:
                                    col_og = col+1
                                    c_og = c+2
                                elif col==1 and c==0:
                                    col_og = col+1
                                    c_og = c+1
                                elif col==1 and c==1:
                                    col_og = col+1
                                    c_og = c+2
                                elif col==2:
                                    col_og = col+1
                                    c_og = c+1
                                # append into conflicting list
                                conflicting.append([temp, temp_in, col_og, 'to', c_og])
            # same as above if
            # if encountered write then it will check for write in inner matrix
            elif 'W' in temp:
                matrix_copy = matrix
                matrix_copy2 = matrix[row+1:,:]
                matrix_copy2 = np.delete(matrix_copy2, col, axis=1)
                row_in, col_in = matrix_copy2.shape
                
                # only forward and below matrix pass
                for r in range(row_in):
                    for c in range(col_in):
                        if matrix_copy2[r, c] != 0:
                            temp_in = matrix_copy2[r, c]
                            temp_in_o = temp_in[0]
                            temp_in_e = temp_in[1]
                            
                            #if (("Write" or "WRITE" or "W" or "w" or "write") in temp_in) and (temp_e==temp_in_e):
                            if temp_in_o == 'W' and temp_e==temp_in_e:
                                if col==0:
                                    col_og = col+1
                                    c_og = c+2
                                elif col==1 and c==0:
                                    col_og = col+1
                                    c_og = c+1
                                elif col==1 and c==1:
                                    col_og = col+1
                                    c_og = c+2
                                elif col==2:
                                    col_og = col+1
                                    c_og = c+1
                                # append into list
                                conflicting.append([temp, temp_in, col_og, 'to', c_og])

print("\nYour Schedule:")
print(matrix)
print("\nConflicting pairs:")
for i in conflicting:
    print(i)

# to check cycle
cyclic_list = []
no_duplicates_cyclic = []
for i in conflicting:
    cyclic_list.append([i[2],i[4]])
    
# remove duplicates from cyclic list so that we can then check for cycle
no_duplicates_cyclic = []
for i in cyclic_list:
    if i not in no_duplicates_cyclic:
        no_duplicates_cyclic.append(i)
# convert cyclic list into array and then reshaping into 2col xrows for convenience
cyclic_arr = np.array(no_duplicates_cyclic)
cyclic_matrix = cyclic_arr.reshape(len(no_duplicates_cyclic),2)
print("\nTo plot graph use below: ")
print(cyclic_matrix)

# condition to check cycle
'''cyclic = True
for i in range(len(cyclic_matrix)-1, 0, -1):
    for j in range(1, len(cyclic_matrix)):
        if i>j:
            if cyclic_matrix[i][0] == cyclic_matrix[i-j][0]:
                cyclic = False
            else:
                cyclic = True'''
counter = 0
for i in range(len(cyclic_matrix)-1, 0, -1):
    for j in range(1, len(cyclic_matrix)):
            if cyclic_matrix[i][0] != cyclic_matrix[i-j][0]:
                counter += 1
            else:
                counter -= 1
if counter>=3 :
    cyclic = True
else:
    cyclic = False
    
if cyclic== True:
    print("\nThe graph is Cyclic i.e the Schedule IS NOT conflict serializable")
elif cyclic==False :
    print("\nThe graph is NOT Cyclic i.e the Schedule IS conflict serializable")

# to calculate indegree of each transaction
indegree = []
for i in cyclic_list:
    if i not in indegree:
        indegree.append(i)
# counting indegree for each transaction for convenience
indeg = []
for i in indegree:
    indeg.append(i[1])
t1 = indeg.count(1)
t2 = indeg.count(2)
t3 = indeg.count(3)
indeg = [t1, t2, t3]

print()
for i in range(len(indeg)):
    print("Indegree of T{} is : {}".format(i+1, indeg[i]))
