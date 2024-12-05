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
    is_valid = True
    for i in range(len(manual)):
        for rule in rule_list:
            ''' 
            es.
            manual: 75,47,61,53,29
            rule: 75|53 -> (75 > 53)
            '''
            if manual[i] == rule[0] and rule[1] in manual[:i]: 
                is_valid = False
    if is_valid:   
        valid_manuals.append(manual)         

#print(valid_manuals)

sum = 0
for i in valid_manuals:
    sum += int(i[int(len(i)/2)])

print(sum)
