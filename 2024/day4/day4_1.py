import numpy as np

with open('./input.txt', 'r') as file_in:
    txt = [*str(file_in.read()).replace('\n','')]

matrice = np.array(txt).reshape(140,140)


# orizontal and vertical
tot = 0
for i in matrice:
    tot += ''.join(i).count('XMAS') + ''.join(i).count('SAMX')

for i in np.rot90(matrice):
    tot += ''.join(i).count('XMAS') + ''.join(i).count('SAMX')


# diagonals
# up left -> down rigth
for i in range(-int(len(matrice[0])), int(len(matrice[0]))):
    tot += ''.join(np.diag(matrice, k=i)).count('XMAS') + ''.join(np.diag(matrice, k=i)).count('SAMX')

mat_rot = np.rot90(matrice)

# up rigth -> down left
for i in range(-int(len(mat_rot[0])), int(len(mat_rot[0]))):
    tot += ''.join(np.diag(mat_rot, k=i)).count('XMAS') + ''.join(np.diag(mat_rot, k=i)).count('SAMX')

print(tot)

