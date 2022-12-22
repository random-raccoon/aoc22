from functools import cmp_to_key

def parse(line):
    value = []
    current_list = value
    stack = []
    line = line[1:-1]

    num = 0
    has_num = False
    for c in line:
        if c == '[':
            l = []
            stack.append(current_list)
            current_list.append(l)
            current_list = l
            num = 0
        elif c == ']':
            if has_num:
                current_list.append(num)
                has_num = False
                num = 0
            current_list = stack.pop()
        elif c == ',':
            if has_num:
                current_list.append(num)
                num = 0
                has_num = False
        else:
            num = num * 10 + int(c)
            has_num = True

    if has_num:
        current_list.append(num)

    return value

def compare(left, right):
    for i in range(0, min(len(left), len(right))):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
        else:
            if isinstance(left[i], int):
                left[i] = [left[i]]
            if isinstance(right[i], int):
                right[i] = [right[i]]
            retval = compare(left[i], right[i])
            if retval != 0:
                return retval
    if len(left) < len(right):
        return 1
    if len(left) > len(right):
        return -1
    return 0

with open('13/input.txt', 'r') as f:
    lines = f.readlines()
    num_pairs = (len(lines) + 1) // 3

    signals = []

    for i in range(0, num_pairs):
        signals.append(parse(lines[i * 3].strip()))
        signals.append(parse(lines[i * 3 + 1].strip()))

    divider_a = [[2]]
    divider_b = [[6]]

    signals.append(divider_a)
    signals.append(divider_b)

    signals.sort(key=cmp_to_key(compare), reverse=True)

    index = 0
    answer = 1
    for signal in signals:
        index += 1
        if signal == divider_a or signal == divider_b:
            answer *= index

    print(answer)