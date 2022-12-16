def isValid(grid, r, c):
    # Gross.
    height = len(grid)
    width = len(grid[0])
    return r >= 0 and c >= 0 and r < height and c < width

def calcView(grid, r, c):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    score = 1
    height = grid[r][c]
    for d in dirs:
        dist = 0
        (dr, dc) = d
        while True:
            if not isValid(grid, r+dr, c + dc):
                break
            dist += 1
            if grid[r+dr][c+dc] >= height:
                break
            (dr, dc) = (dr + d[0], dc + d[1])
        score *= dist            
    return score

with open('08/input.txt', 'r') as f:
    grid = [[int(c) for c in l.strip()] for l in f.readlines()]
    height = len(grid)
    width = len(grid[0])

    visible = [[False for i in range(0, width)] for j in range(0, height)]

    for r in range(0,height):
        blockingHeight = -1
        for c in range(0,width):
            if grid[r][c] > blockingHeight:
                visible[r][c] = True
                blockingHeight = grid[r][c]

    for r in range(0,height):
        blockingHeight = -1
        for c in range(width-1, -1, -1):
            if grid[r][c] > blockingHeight:
                visible[r][c] = True
                blockingHeight = grid[r][c]

    for c in range(0,width):
        blockingHeight = -1
        for r in range(0,height):
            if grid[r][c] > blockingHeight:
                visible[r][c] = True
                blockingHeight = grid[r][c]

    for c in range(0,width):
        blockingHeight = -1
        for r in range(height-1, -1, -1):
            if grid[r][c] > blockingHeight:
                visible[r][c] = True
                blockingHeight = grid[r][c]

    bestView = 0
    # Brute force, baby.  But took WAY less than a second so...
    for r in range(0, height):
        for c in range(0, width):
            if visible[r][c]:
                view = calcView(grid, r, c)
                bestView = max(view, bestView)

    print(bestView)
