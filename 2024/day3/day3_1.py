import re

with open('./input.txt', 'r') as file_in:
    txt = file_in.read()

out = re.findall(r'mul\((\d+),(\d+)\)', txt)

result = 0
for i in out:
    result += int(i[0]) * int(i[1])

print(result)
