sequence = []

starting_pos = 50
current_pos = starting_pos
zero_count = 0

with open("./input.txt") as file:
    for line in file:
        sequence.append((line.strip()[0], line.strip()[1:]))

temp_pos = current_pos
for i in sequence:
    temp_pos = current_pos
    if i[0] == 'R':
        for r in range(int(i[1])): 
            current_pos = (current_pos + 1)%100
            if current_pos == 0: zero_count+=1  
    else: 
        for r in range(int(i[1])): 
            current_pos = (current_pos - 1)%100
            if current_pos == 0: zero_count+=1
    
print(zero_count)