moves = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,  # win
    'Y': 1,  # tie
    'Z': 2,  # lose
}
moveGuide = [[2,0,1],
             [0,1,2],
             [1,2,0]]

scores = {'X': 0, 'Y': 3, 'Z': 6}

score = 0

with open('02/input.txt', 'r') as f:
    for line in f:
        [move, outcome] = line.strip().split(' ')
        outcomeIndex = moves[outcome]
        responseIndex = moveGuide[moves[move]][outcomeIndex]
        score += responseIndex + 1
        score += scores[outcome]

print(score)
