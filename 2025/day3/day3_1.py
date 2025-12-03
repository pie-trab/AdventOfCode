lines = []
sum = 0

with open("input.txt") as file:
    for line in file:
        lines.append(list(line.strip()))
        
for line in lines:
    max1 = -1
    for i in line:
        for j in line[line.index(i)+1:]:
            if int(i+j) > max1:
                max1 = int(i+j)
    sum += max1
            
print(sum)    
        
            
    
