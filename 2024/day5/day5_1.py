rule_list = []
manual_list = []

with open('./sample.txt', 'r') as file:
    while line := file.readline():
        if not line.strip(): continue
        if '|' in line:
            rule_list.append((line.strip().split('|')[0], line.strip().split('|')[1]))
        else:
            manual_list.append(line.strip().split(','))


for manual in manual_list:
    for i in range(len(manual)):
        for rule in rule_list:
            ''' 
            es.
            manual: 75,47,61,53,29
            rule: 75|53 -> (75>53)
            '''
            if manual[i] in rule[0] and rule[1] in manual:
                
    
    


