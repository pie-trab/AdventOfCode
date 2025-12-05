def get_neighbours(matrix, row, col):
    neighbours = []
    if row - 1 >= 0:
        neighbours.append(matrix[row-1][col])
        if col - 1 >= 0: neighbours.append(matrix[row-1][col-1])
        if col + 1 < len(matrix[0]): neighbours.append(matrix[row-1][col+1])
    if col - 1 >= 0: neighbours.append(matrix[row][col-1])
    if col + 1 < len(matrix[0]): neighbours.append(matrix[row][col+1])
    if row + 1 < len(matrix):
        neighbours.append(matrix[row+1][col])
        if col - 1 >= 0: neighbours.append(matrix[row+1][col-1])
        if col + 1 < len(matrix[0]): neighbours.append(matrix[row+1][col+1])     
    
    return neighbours  

matrix = []

with open("input.txt") as file:
    for line in file:
        matrix.append(list(line.strip()))

to_remove = [["."] * len(matrix[0])] * len(matrix)

count = 0
flag = True
while flag:
    flag = False
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != "@": continue
            if get_neighbours(matrix, row, col).count("@") < 4: 
                matrix[row][col] = "x"
                count+=1
                flag = True
                    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if to_remove[row][col] == "x": matrix[row][col] = "." 
    
print(count)