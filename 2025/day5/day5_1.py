allowed_set = set()
ingredients_ranges = []
ingredients = []

with open("input.txt") as file:
    for line in file:
        if line == "\n": 
            for ingredient in file:
                ingredients.append(int(ingredient.strip()))
            break    
        ingredients_ranges.append(line.strip().split("-"))

count = 0
for i in ingredients:
    for range in ingredients_ranges:
        if i >= int(range[0]) and i <= int(range[1]): 
            count+=1
            break

print(count)