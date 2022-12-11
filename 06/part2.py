MARKER_LENGTH = 14

with open('06/input.txt', 'r') as f:
    i = 0
    buffer = [' ' for i in range(MARKER_LENGTH)]
    markerFound = False
    while not markerFound:
        buffer[i % MARKER_LENGTH] = f.read(1)
        i += 1
        if i >= MARKER_LENGTH and len(set(buffer)) == MARKER_LENGTH:
            markerFound = True

    print(i)