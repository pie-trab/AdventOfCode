report_list = []

with open('./input.txt') as file:
    for line in file:
        report_list.append([int(elem) for elem in line.split()])

for rep in report_list:
    is_increasing = False
    for i in range(len(rep) - 1):
        # next equal to previous
        if rep[i] == rep[i + 1]: break

        # check for the order
        if i == 0:
            if rep[i + 1] > rep[i]:
                is_increasing = True
            else:
                is_increasing = False
        
        # if increasing and previous was decreasing invalid
        if rep[i + 1] > rep[i] and not is_increasing: break
        # if decreasing and previous was increasing invalid
        if rep[i + 1] < rep[i] and is_increasing: break
        # if distance is greater than 3
        if rep[i + 1] - rep[i] > 3: break



print(report_list)