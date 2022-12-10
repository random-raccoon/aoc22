def toShelves(p):
    [start, end] = [int(num) for num in p.split('-')]
    return set(shelf for shelf in range(start, end+1))

count = 0
with open('04/input.txt', 'r') as f:
    for line in f:
        assignments = [toShelves(part) for part in line.strip().split(',')]
        overlaps = len(assignments[0].intersection(assignments[1])) > 0
        if overlaps:
            count += 1

print(count)