import numpy as np
import re
from scipy.ndimage import rotate

def arr_to_str(arr: list):
    return ''.join(arr)


def find_skewed(matrix: list):
    


with open('./input.txt', 'r') as file_in:
    txt = [*str(file_in.read()).replace('\n','')]

matrix = np.array(txt).reshape(140,140)


total_sum = 0
for count in range(3):
    for i in matrix:
        total_sum += len(re.findall(r'XMAS', arr_to_str(i)))
        total_sum += len(re.findall(r'XMAS', arr_to_str(i)[::-1]))
    
    total_sum += find_skewed(matrix)
    print(matrix)
    matrix = np.rot90(matrix)
    print('-------')



print(total_sum)
