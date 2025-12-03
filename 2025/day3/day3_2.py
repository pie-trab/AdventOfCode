lines = []
sum = 0

with open("input.txt") as file:
    for line in file:
        lines.append(list(line.strip()))
        
for line in lines:
    end = len(line) - 11 # making sure that i have enough digits to complete the number
    digits = []
    while len(digits) < 12:
        max_digit = str(max(line[0:end])) 
        line = line[line.index(max_digit)+1:]
        digits.append(max_digit)
        end = len(line) - (11 - len(digits)) # reduce the number of digits needed
    sum += int(''.join(digits))
       
print(sum)    
        
            
    
