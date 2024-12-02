report_list = []

with open('./input.txt') as file:
    for line in file:
        report_list.append([int(elem) for elem in line.split()])


count = 0
for rep in report_list:
    is_increasing = False
    is_valid = True
    for i in range(len(rep) - 1):
        # next equal to previous
        if rep[i] == rep[i + 1]: 
            is_valid = False
            break

        # check for the order
        if i == 0:
            if rep[i + 1] > rep[i]:
                is_increasing = True
            else:
                is_increasing = False
        
        # if increasing and previous was decreasing invalid
        if rep[i + 1] > rep[i] and not is_increasing: 
            is_valid = False
            break
        # if decreasing and previous was increasing invalid
        if rep[i + 1] < rep[i] and is_increasing: 
            is_valid = False
            break
        # if distance is greater than 3
        if is_increasing and rep[i + 1] - rep[i] > 3 or not is_increasing and rep[i] - rep[i + 1] > 3: 
            is_valid = False
            break
    if is_valid: 
        count += 1

print(count)