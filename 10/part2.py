class Computer:
    def __init__(self):
        self.cycleCount = 0
        self.x = 1
        self.answer = []

    def tick(self):
        crt = self.cycleCount % 40
        if abs(self.x - crt) <= 1:
            self.answer.append('#')
        else:
            self.answer.append('.')
        self.cycleCount += 1
        if self.cycleCount % 40 == 0:
            self.answer.append('\n')


    def noop(self):
        self.tick()

    def addx(self, v):
        self.tick()
        self.tick()
        self.x += v


with open('10/input.txt', 'r')  as f:
    c = Computer()
    for line in f:
        parts = line.strip().split(' ')
        if parts[0] == 'noop':
            c.noop()
        elif parts[0] == 'addx':
            v = int(parts[1])
            c.addx(v)
        else:
            print(f'unknown opcode: {parts[0]}')

    print(''.join(c.answer))