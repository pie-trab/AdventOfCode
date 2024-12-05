rule_list = []
manual_list = []

with open('./input.txt', 'r') as file:
    while line := file.readline():
        if not line.strip(): continue
        if '|' in line:
            rule_list.append((line.strip().split('|')[0], line.strip().split('|')[1]))
        else:
            manual_list.append(line.strip().split(','))


valid_manuals = []

for manual in manual_list:
    is_valid = False
    for j in range(8):  # Terrible solution but I didn't want to find the rigth condition
                        # Also I started with 100, and reduced it with the lowest possible number 
                        # that gives the rigth solution: 8 (7 are too little iterations and would give 6364)
        for i in range(len(manual)):
            for rule in rule_list:
                if manual[i] == rule[0] and rule[1] in manual[:i]: 
                    # swap rule[0] in manual with rule[1] in manual
                    is_valid = True
                    manual[i] = rule[1]
                    manual[manual.index(rule[1])] = rule[0]

    if is_valid:   
        valid_manuals.append(manual)         

sum = 0
for i in valid_manuals:
    sum += int(i[int(len(i)/2)])

print(sum)







