import time
ingredients_ranges = []

with open("input.txt") as file:
    for line in file:
        if line == "\n": 
            break    
        ingredients_ranges.append([int(line.strip().split("-")[0]), int(line.strip().split("-")[1])])
            
ingredients_ranges = sorted(ingredients_ranges)

total_range = []

start = ingredients_ranges[0][0]
end = ingredients_ranges[0][1]

for i in ingredients_ranges[1:]: 
    if i[0] > end: 
        total_range.append([start, end])
        start = i[0]
        end = i[1]
        continue
    if i[0] <= end:
        if i[1] > end: end = i[1]
        else: continue

total_range.append([start, end])

sum = 0
for i in total_range:
    sum += i[1] - i[0] + 1 

print(sum)