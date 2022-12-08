calories = []
with open("01/input.txt", "r") as f:
    count = 0
    for line in f:
        if line.strip():
            count += int(line)
        else:
            calories.append(count)
            count = 0
    calories.append(count)

calories.sort()
print(sum(calories[-3:]))