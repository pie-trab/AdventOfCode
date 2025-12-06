lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(line.strip().split(" "))


operators = [[item for item in x if item] for x in lines[-1:]][0]
lines = [[item for item in x if item] for x in lines[:-1]]

results = [int(item) for item in lines[0]]
for i, line in enumerate(lines[1:]):
    for j, num in enumerate(line):
        if operators[j] == "*": results[j] *= int(num)
        if operators[j] == "+": results[j] += int(num)


print(sum(results))