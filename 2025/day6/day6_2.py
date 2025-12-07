lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(line.strip('\n'))

operators = lines[-1] + " "
lines = lines[:-1]

sizes = []
count = 0
for i in operators[::-1]:
    count+=1
    if i != " ": 
        # (size, operator)
        sizes.append((count-1, i))
        count = 0
        
sizes = sizes[::-1]

numbers = []
for line in lines:
    start = 0
    end = 0
    count = 0
    line_list = []
    for i in range(len(sizes)):
        end = sizes[i][0]+count
        line_list.append(line[start:end])
        count += len(line[start:end]) + 1
        start = count
    numbers.append(line_list)

columns = [[] for _ in range(len(numbers[0]))]

for line in numbers:
    for i, number in enumerate(line):
        columns[i].append(number)

total = 0
for i, col in enumerate(columns):
    if sizes[i][1] == "*": sum = 1
    if sizes[i][1] == "+": sum = 0
    for j in range(sizes[i][0]):
        partial = ""
        for n in range(len(col)):
            partial += col[n][j]
        if sizes[i][1] == "*": sum *= int(partial.strip())
        if sizes[i][1] == "+": sum += int(partial.strip())
    total+=sum

print(total)


