DIR_MAP = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
}

def update(a, b):
    if touching(a, b):
        return b
    return moveTail(a, b)

# Diagonal counts.
def touching(a, b):
    return abs(a[1] - b[1]) <= 1 and abs(a[0] - b[0]) <= 1

def moveTail(head, tail):
    dx = min(max(head[0] - tail[0], -1), 1)
    dy = min(max(head[1] - tail[1], -1), 1)
    return (tail[0] + dx, tail[1] + dy)

nodes = [(0, 0) for i in range(0, 10)]
visited = set()
visited.add((0,0))

with open('09/input.txt', 'r') as f:
    for line in f:
        (direction, steps) = line.strip().split(' ')
        steps = int(steps)
        for i in range(0, steps):
            nodes[0] = (nodes[0][0] + DIR_MAP[direction][0], nodes[0][1] + DIR_MAP[direction][1])
            for j in range(1, 10):
                nodes[j] = update(nodes[j-1], nodes[j])
            visited.add(nodes[9])

print(len(visited))