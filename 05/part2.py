# Thank goodness we're limiting to single digit column numbers!
import re

with open('05/input.txt', 'r') as f:
    line = f.readline()
    numStacks = len(line) // 4
    stacks = [[] for i in range(numStacks)]

    # Read in the contents of the stacks.
    while line != '\n':
        for i in range(numStacks):
            c = line[i * 4 + 1]
            if c != ' ':
                stacks[i].append(c)
        line = f.readline()

    # Remove the stack numbers
    stacks = [stack[:-1] for stack in stacks]
    # Reverse them so that the top of the stack is the end of the list.
    for stack in stacks:
        stack.reverse()

    instructions = f.readlines()
    crane = []
    for instruction in instructions:
        parts = re.search('move (.*) from (.) to (.)', instruction).groups()
        num = int(parts[0])
        source = int(parts[1]) - 1
        dest = int(parts[2]) - 1

        for i in range(num):
            crane.append(stacks[source].pop())
        for i in range(num):
            stacks[dest].append(crane.pop())

    message = ''.join([stack[-1] for stack in stacks])
    print(message)