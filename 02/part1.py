moves = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2,
}
scoreGuide = [[3,6,0],
              [0,3,6],
              [6,0,3]]

score = 0

with open('02/input.txt', 'r') as f:
    for line in f:
        [move, response] = line.strip().split(' ')
        score += moves[response] + 1
        score += scoreGuide[moves[move]][moves[response]]

print(score)
