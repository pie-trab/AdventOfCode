lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(list(line.strip()))    
        
for i in lines:
    for j in range(len(i)):
        if i[j] == '.':
            i[j] = 0

count = 0
for i in range(len(lines) -1):
    for j, ch in enumerate(lines[i]):
        if type(ch) == str:
            if ch == "S": lines[i+1][j] +=1
            if ch == "^": 
                lines[i][j+1] += lines[i-1][j]
                lines[i][j-1] += lines[i-1][j]
                k = 1
                while(type(lines[i+k][j+1]) != str): 
                    lines[i+k][j+1] += lines[i-1][j]
                    k+=1
                k = 1
                while(type(lines[i+k][j-1]) != str or k == len(lines)): 
                    lines[i+k][j-1] += lines[i-1][j]
                    k+=1 
  
for i in lines: 
    for c in i:
        print(str(c)+' ', end='')
    print("")
    
print(max(lines[-1]))