import numpy as np

def matrixMulti(m1,m2):
    # handle incompatible matrix dimensions
    if len(m1[0]) != len(m2):
        print("Matrix A and B are not compatible for multiplication.\n")
        return
    
    m3 = []
    
    # Dot product (a,b)x(c,d)= ab + cd
    for i in range(len(m1)):
        m3_row=[]
        for j in range(len(m2[0])):
            a = 0
            for k in range(len(m2)):
                a+=m1[i][k]*m2[k][j]
            m3_row.append(a)
        m3.append(m3_row)
        
    # return any succesful matrix multiplications
    print("The resulting matrix of A * B is:\n")
    printMatrix(m3)
    return m3

def matrixAdd(m1,m2):
    # handle incompatible matrix dimensions
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        print("The dimensions of Matrix A and B are not compatible for addition or subtraction.\n")
        return
    
    # Add each element in matching cell locations in array m3
    m3 = []
    # We iterate through each row and collumn
    for row in range(len(m1)):
        m3_row = []
        for col in range(len(m1[0])):
            m3_row.append(m1[row][col]+m2[row][col])
        m3.append(m3_row)
    
    # Print and return any succcessful additions
    print("The resulting matrix of A + B is:\n")
    return printMatrix(m3)

def matrixSub(m1,m2):
    # handle incompatible matrix dimensions
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        print("The dimensions of Matrix A and B are not compatible for addition or subtraction.\n")
        return
    
    # Subtract each element in matching cell locations in array m3
    m3=[]
    # We iterate through each row and collumn
    for row in range(len(m1)):
        # we append m3 row by row
        m3_row = []
        for col in range(len(m1[0])):
            # we append each row col by col
            m3_row.append(m1[row][col]-m2[row][col])
        m3.append(m3_row)
        
    # return the resulting matrix and print it
    print("The resulting matrix of A - B is:\n")
    return printMatrix(m3)

def printMatrix(m):
    # prints the matrix in a readable format
    for row in m:
        print(row)
    
    print()
    return

rows_a = int(input("Please enter the row size of Matrix A: "))
cols_a = int(input("Please enter the collumn size of Matrix A: "))

rows_b = int(input("\nPlease enter the row size of Matrix B: "))
cols_b = int(input("Please enter the collumn size of Matrix B: "))

matrixA = []
matrixB = []
print()
# The user fills in Matrix A
for i in range(rows_a):
    row = []
    for j in range(cols_a):
        element = int(input(f"Enter element for position ({i},{j}): "))
        row.append(element)
    matrixA.append(row)

# The user fills in Matrix B
for i in range(rows_b):
    row = []
    for j in range(cols_b):
        element = int(input(f"Enter element for position ({i},{j}): "))
        row.append(element)
    matrixB.append(row)

print("\nMatrix A\n")
printMatrix(matrixA)
print("Matrix B\n")
printMatrix(matrixB)
print("Calculating Addition, Subtraction, and Multiplication for Matricies A and B...\n")
matrixAdd(matrixA,matrixB)
matrixSub(matrixA,matrixB)
matrixMulti(matrixA,matrixB)

# Calculatinng the inverse of any 4x4 matrix

# Fill in the matrix with user input
print("Input values for a 4x4 matrix.\n")
m_4x4 = []
for i in range(4):
    row = []
    for j in range(4):
        element = float(input(f"Enter element for position ({i},{j}): "))
        row.append(element)
    m_4x4.append(row)
    
# I will be using the numpy library for efficiency
inv_m = np.linalg.inv(m_4x4)  
print("This is the inverse of your matrix.\n")
printMatrix(inv_m)