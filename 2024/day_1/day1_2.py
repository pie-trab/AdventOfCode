list1 = []
list2 = []

with open('./input.txt') as file:
    for line in file:
        list1.append(line.strip().split()[0])
        list2.append(line.strip().split()[1])

list2.sort()

freq_list2 = {}

temp = list2[0]
for key in list2:
    if not key in freq_list2.keys():
        freq_list2[key] = 1
    else: 
        freq_list2[key] = freq_list2[key] + 1

similarity_score = 0

for elem in list1:
    if elem in freq_list2.keys():
        similarity_score += int(elem) * freq_list2[elem] 
    
print(similarity_score)