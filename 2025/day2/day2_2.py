rage_list = []
total = 0

with open('input.txt') as file:
    for line in file:
        rage_list = line.split(',')

pattern_flag = True

for i in rage_list:
    for j in range(int(i.split('-')[0]), int(i.split('-')[1])+1):
        for k in range(1,len(str(j))//2 + 1):
            pattern = str(j)[0:k]
            pattern_flag = True
            for z in range(0,len(str(j)),len(pattern)):
                if str(j)[z:z+len(pattern)] != pattern:
                    pattern_flag = False
                    break
            if pattern_flag:
                total += j    
                break  
            
print(total)        
        
        