import heapq

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

class Map:
    def __init__(self, lines):
        self.data = [[ord(c) - ord('a') for c in line.strip()] for line in lines]
        start = ord('S') - ord('a')
        dest = ord('E') - ord('a')
        self.width = len(self.data)
        self.height = len(self.data[0])
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.data[x][y] == start:
                    self.data[x][y] = 0
                    self.start = (x, y)
                elif self.data[x][y] == dest:
                    self.data[x][y] = ord('z') - ord('a')
                    self.dest = (x, y)

    def canMove(self, pos, d):
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if new_pos[0] < 0 or new_pos[0] >= self.width:
            return False
        if new_pos[1] < 0 or new_pos[1] >= self.height:
            return False
        if self.data[new_pos[0]][new_pos[1]] - self.data[pos[0]][pos[1]] < -1:
            return False
        return True

    def solve(self):
        paths = []
        heapq.heappush(paths, (26, self.dest, 0))

        best_path_lenghts = {
            self.dest: 0,
        }
        while True:
            (cost, pos, path_len) = heapq.heappop(paths)
            for d in DIRS:
                if self.canMove(pos, d):
                    new_pos = (pos[0] + d[0], pos[1] + d[1])
                    new_path_len = path_len + 1
                    if self.data[new_pos[0]][new_pos[1]] == 0:
                        return new_path_len
                    cost = new_path_len + self.data[new_pos[0]][new_pos[1]]  # Prefer to be lower
                    if new_pos in best_path_lenghts:
                        if best_path_lenghts[new_pos] <= new_path_len:
                            continue
                        paths = [path for path in paths if path[1] != new_pos]
                        heapq.heapify(paths)
                    heapq.heappush(paths, (cost, new_pos, new_path_len))
                    best_path_lenghts[new_pos] = new_path_len
                        

with open('12/input.txt', 'r') as f:
    map = Map(f.readlines())
    path = map.solve()
    print(path)