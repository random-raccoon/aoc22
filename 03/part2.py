def priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
    return 0

score = 0

with open('03/input.txt', 'r') as f:
    stage = 0
    overlap = set()
    for line in f:
        contents = set(line.strip())
        if stage == 0:
            overlap = contents
            stage = 1
        elif stage == 1:
            overlap = overlap.intersection(contents)
            stage = 2
        else:
            overlap = overlap.intersection(contents)
            for c in overlap:
                score += priority(c)
            stage = 0

print(score)