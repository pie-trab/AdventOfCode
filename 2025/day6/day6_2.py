import numpy as np

lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(line.strip().split(" "))


operators = [[item for item in x if item] for x in lines[-1:]][0]
lines = [[item for item in x if item] for x in lines[:-1]]

maxes = [-1] * len(lines[0])
for i in lines:
    for index, j in enumerate(i):
        if len(j) > maxes[index]: maxes[index] = len(j) 

print(maxes)

for i, line in enumerate(lines):
    for j, num in enumerate(line):
        lines[i][j] = num.rjust(maxes[j], '0')


print(lines)

'''
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
'''

results = [int(item) for item in lines[0]]
partial = []
for j in range(len(lines[0])):
    a = []
    for i in range(len(lines)):
        a.append(lines[i][j])
    partial.append(a)




'''
            if operators[j] == "*": results[j] *= int(num)
            if operators[j] == "+": results[j] += int(num)
'''