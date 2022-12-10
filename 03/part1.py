def priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
    return 0

score = 0

with open('03/input.txt', 'r') as f:
    for line in f:
        contents = line.strip()
        half = len(contents)//2
        parts = [set(contents[:half]), set(contents[half:])]
        overlap = parts[0].intersection(parts[1])
        
        # assertion (unchecked): exactly one item exists in overlap.
        for c in overlap:
            score += priority(c)

print(score)