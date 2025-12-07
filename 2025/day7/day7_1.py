lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(list(line.strip()))    

count = 0
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if i > 0:
            if (lines[i-1][j] == "S" or lines[i-1][j] == "|") and ch != "^":
                lines[i][j] = "|"
            if lines[i-1][j] == "|" and ch == "^":
                count += 1
                lines[i][j-1] = "|"
                lines[i][j+1] = "|" 
  
print(count)