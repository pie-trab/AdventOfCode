report_list = []

with open('./input.txt') as file:
    for line in file:
        report_list.append([int(elem) for elem in line.split()])

# recursively checks the lenght and return if at the second check the 
# condition is also false
def check_distance(rep: list, is_increasing: bool, first_iter: bool=True):
    for i in range(len(rep) - 1):
        if is_increasing and rep[i + 1] - rep[i] > 3:
            if first_iter:
                rep.remove(rep[i+1])
                return check_distance(rep, is_increasing, False)
            else: return False
        elif not is_increasing and rep[i] - rep[i + 1] > 3:
            if first_iter:
                rep.remove(rep[i+1])
                return check_distance(rep, is_increasing, False)
            else: return False

    return True



count = 0
for rep in report_list:
    is_increasing = False
    is_valid = 0
    for i in range(len(rep) - 1):
        # next equal to previous
        if rep[i] == rep[i + 1]: 
            is_valid += 1
        
        # check for the order
        if i == 0:
            if rep[i + 1] > rep[i]:
                is_increasing = True
            else:
                is_increasing = False
        
        # if increasing and previous was decreasing -> invalid
        if rep[i + 1] > rep[i] and not is_increasing: 
            is_valid += 1 
            
        # if decreasing and previous was increasing -> invalid
        if rep[i + 1] < rep[i] and is_increasing: 
            is_valid += 1
         
    # if 0 or 1 checks are false, and also the distances are rigth increase the count
    if is_valid < 2 and check_distance(rep, is_increasing):
        count += 1
    
print(count)