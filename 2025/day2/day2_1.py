rage_list = []
total = 0

with open('input.txt') as file:
    for line in file:
        rage_list = line.split(',')

for i in rage_list:
    for j in range(int(i.split('-')[0]), int(i.split('-')[1])+1):
        if len(str(j)) % 2 == 0 and str(j)[len(str(j))//2:] == str(j)[:len(str(j))//2]:
            total += j
            
print(total)        
        
        