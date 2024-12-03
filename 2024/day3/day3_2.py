import re

with open('./input.txt', 'r') as file_in:
    txt = file_in.read()

mul_reg = r'mul\((\d+),(\d+)\)'
do_reg = r'do\(\)'
dont_reg = r'don\'t\(\)'

out = re.compile('(%s|%s|%s)' % (mul_reg, do_reg, dont_reg)).findall(txt)

ignore = False
result = 0
for i in out:
    if i[0] == "don't()":
        ignore = True
        continue
    elif i[0] == "do()":
        ignore = False
        continue

    if not ignore:
        result += int(i[1])*int(i[2])

print(result)