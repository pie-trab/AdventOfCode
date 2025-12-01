sequence = []

starting_pos = 50

with open("./input.txt") as file:
    for line in file:
        sequence.append({line.strip()[0], line.strip()[1:]})

print(sequence)

print((99+10+100)%100)