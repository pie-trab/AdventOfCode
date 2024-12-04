import numpy as np

with open('./input.txt', 'r') as file_in:
    txt = [*str(file_in.read()).replace('\n','')]

matrice = np.array(txt).reshape(140,140)
tot_sum = 0
for row in range(len(matrice[0])-1):
    for col in range(len(matrice[0])-1):
        if matrice[row][col] == 'A':
            if ((matrice[row+1][col+1] == 'M' and matrice[row-1][col-1] == 'S' or
                matrice[row+1][col+1] == 'S' and matrice[row-1][col-1] == 'M') and 
                (matrice[row+1][col-1] == 'M' and matrice[row-1][col+1] == 'S' or
                matrice[row+1][col-1] == 'S' and matrice[row-1][col+1] == 'M')):
                    tot_sum += 1

print(tot_sum)


