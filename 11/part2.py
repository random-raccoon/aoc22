class Monkey:
    def __init__(self, data):
        self.name = data[0].split(':')[0]
        self.items = [int(item) for item in data[1].split(':')[1].strip().split(',')]

        operation = data[2].strip().split(':')[1].split('=')[1].strip()
        self.operator = operation[4]
        operand = operation[6:]
        if operand == 'old':
            self.operator = '2'
        else:
            self.operand = int(operand)

        self.test = int(data[3].strip()[19:])

        self.true_monkey = int(data[4].strip()[-1])
        self.false_monkey = int(data[5].strip()[-1])

        self.inspect_count = 0

    def inspectAll(self, monkeys, monkey_factor):
        for item in self.items:
            new_worry = 0
            if self.operator == '2':
                new_worry = item * item
            elif self.operator == '+':
                new_worry = item + self.operand
            elif self.operator == '*':
                new_worry = item * self.operand
            else:
                print(f'unknown operator: {self.operator}')
            
            # Reduce worry to something a bit more sane.
            new_worry = new_worry % monkey_factor

            if new_worry % self.test == 0:
                monkeys[self.true_monkey].items.append(new_worry)
            else:
                monkeys[self.false_monkey].items.append(new_worry)

        self.inspect_count += len(self.items)
        self.items = []
    
    def __repr__(self):
        return f'{self.name}: {self.items}'


with open('11/input.txt', 'r') as f:
    data = f.readlines()
    # 6 lines of data + 1 empty line in between.
    num_monkeys = (len(data) + 1) // 7
    monkeys = [Monkey(data[i*7:i*7+7]) for i in range(0, num_monkeys)]

    # I know there's a 1-liner here..
    monkey_factor = 1
    for monkey in monkeys:
        monkey_factor *= monkey.test

    for i in range(0, 10000):
        for monkey in monkeys:
            monkey.inspectAll(monkeys, monkey_factor)

    inspect_counts = [monkey.inspect_count for monkey in monkeys]
    print(inspect_counts)
    inspect_counts.sort()
    print(inspect_counts[-1] * inspect_counts[-2])