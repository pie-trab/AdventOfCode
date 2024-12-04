import numpy as np
import re

def arr_to_str(arr: list):
    return ''.join(arr)
   
with open('./sample_in.txt', 'r') as file_in:
    txt = [*str(file_in.read()).replace('\n','')]

matrix = np.array(txt).reshape(10,10)

def find_orizontal(matrix:list):
    tot_sum = 0

    for row in matrix:
        str_row = arr_to_str(row)
        tot_sum += str_row.count('XMAS') + str_row.count('SAMX')
    
    rot_mat = np.rot90(matrix)

    for row in matrix:
        str_row = arr_to_str(row)
        tot_sum += str_row.count('XMAS') + str_row.count('SAMX')

    return tot_sum





total_sum = find_orizontal(matrix)
#total_sum += find_skewed(matrix)

print(total_sum)