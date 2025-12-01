sequence = []

starting_pos = 50
current_pos = starting_pos
zero_count = 0

with open("./input.txt") as file:
    for line in file:
        sequence.append((line.strip()[0], line.strip()[1:]))

for i in sequence:
    if i[0] == 'R':
        current_pos = (current_pos + int(i[1]))%100
    else: 
        current_pos = (current_pos - int(i[1]))%100
    if current_pos == 0: zero_count += 1

print(zero_count)