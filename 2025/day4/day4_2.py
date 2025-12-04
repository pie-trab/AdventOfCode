import numpy as np

def get_neighbours(matrix, row, col):
    neighbours = []
    if row - 1 >= 0:
        neighbours.append(matrix[row-1][col])
        if col - 1 >= 0: neighbours.append(matrix[row-1][col-1])
        if col + 1 < len(matrix[0]): neighbours.append(matrix[row-1][col+1])
    if col - 1 >= 0: neighbours.append(matrix[row][col-1])
    # print("row: " + str(row) + ", col + 1: " + str(col +1) + ", len(matrix[0]): " + str(len(matrix[0])))
    if col + 1 < len(matrix[0]): neighbours.append(matrix[row][col+1])
    if row + 1 < len(matrix):
        neighbours.append(matrix[row+1][col])
        if col - 1 >= 0: neighbours.append(matrix[row+1][col-1])
        if col + 1 < len(matrix[0]): neighbours.append(matrix[row+1][col+1])     
    
    return neighbours  

lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(list(line.strip()))

matrix = lines

to_remove = [["."] * len(matrix[0])] * len(matrix)

count = 0
flag = True
while flag:
    flag = False
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != "@": continue
            # print(get_neighbours(matrix, row, col))
            if get_neighbours(matrix, row, col).count("@") < 4: 
                matrix[row][col] = "x"
                count+=1
                flag = True
    print(count)                
    print(np.matrix(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if to_remove[row][col] == "x": matrix[row][col] = "." 
    
    print(np.matrix(matrix))
    
print(count)
       

