list1 = []
list2 = []

with open('./input.txt') as file:
    for line in file:
        list1.append(line.strip().split()[0])
        list2.append(line.strip().split()[1])
        
list1.sort()
list2.sort()

tot_distance = 0

for i in range(len(list1)):
    tot_distance += abs(int(list1[i]) - int(list2[i]))

print(tot_distance)

    

