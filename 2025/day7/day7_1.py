lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(line)    
    

for i, line in enumerate(lines):
    for j in line:
        if j == "S":
            lines[i+1][j] = "|"
        if j == "^" and line[i-1][j] == "|":
            lines[i][j-1] == "|"
            lines[i][j+1] == "|"
        