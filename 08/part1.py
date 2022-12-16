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

    numVisible = sum([sum([1 for v in r if v]) for r in visible])
    print(numVisible)
