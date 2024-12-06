# TODO

import numpy as np

with open('./sample.txt', 'r') as file_in:
    txt = [*str(file_in.read()).replace('\n', '')]

size = 10
matrix = np.array(txt).reshape(size, size)


def find_initial_pos(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            # print(matrice[row][col])
            if matrix[row][col] == '^':
                return [row, col]
    return -1


curr_pos = find_initial_pos(matrix)
alredy_visited = [(curr_pos[0], curr_pos[1])]
direction = 0  # 0: up, 1: rigth, 2: down, 3: left
in_lab = True
count = 0
while in_lab:
    match direction:
        case 0:
            if curr_pos[0] - 1 < 0:
                in_lab = False
                break
            if matrix[curr_pos[0] - 1][curr_pos[1]] == '#':
                direction = (direction + 1) % 4
            else:
                curr_pos = [curr_pos[0] - 1, curr_pos[1]]
                if (curr_pos[0], curr_pos[1]) in alredy_visited:
                    count += 1
                else:
                    alredy_visited.append((curr_pos[0], curr_pos[1]))
                matrix[curr_pos[0]][curr_pos[1]] = 'O'
        case 1:
            if curr_pos[1] + 1 > size - 1:
                in_lab = False
                break
            if matrix[curr_pos[0]][curr_pos[1] + 1] == '#':
                direction = (direction + 1) % 4
            else:
                curr_pos = [curr_pos[0], curr_pos[1] + 1]
                if (curr_pos[0], curr_pos[1]) in alredy_visited:
                    count += 1
                else:
                    alredy_visited.append((curr_pos[0], curr_pos[1]))
                matrix[curr_pos[0]][curr_pos[1]] = 'O'
        case 2:
            if curr_pos[0] + 1 > size - 1:
                in_lab = False
                break
            if matrix[curr_pos[0] + 1][curr_pos[1]] == '#':
                direction = (direction + 1) % 4
            else:
                curr_pos = [curr_pos[0] + 1, curr_pos[1]]
                if (curr_pos[0], curr_pos[1]) in alredy_visited:
                    count += 1
                else:
                    alredy_visited.append((curr_pos[0], curr_pos[1]))
                matrix[curr_pos[0]][curr_pos[1]] = 'O'
        case 3:
            if curr_pos[1] - 1 < 0:
                in_lab = False
                break
            if matrix[curr_pos[0]][curr_pos[1] - 1] == '#':
                direction = (direction + 1) % 4
            else:
                curr_pos = [curr_pos[0], curr_pos[1] - 1]
                if (curr_pos[0], curr_pos[1]) in alredy_visited:
                    count += 1
                else:
                    alredy_visited.append((curr_pos[0], curr_pos[1]))
                matrix[curr_pos[0]][curr_pos[1]] = 'O'

    print(matrix)  # uncomment to show the path taken each step
print(count)
