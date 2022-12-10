def toShelves(p):
    [start, end] = [int(num) for num in p.split('-')]
    return set(shelf for shelf in range(start, end+1))

count = 0
with open('04/input.txt', 'r') as f:
    for line in f:
        assignments = [toShelves(part) for part in line.strip().split(',')]
        if assignments[0].issubset(assignments[1]) or assignments[1].issubset(assignments[0]):
            count += 1

print(count)