with open('06/input.txt', 'r') as f:
    i = 0
    buffer = [' ' for i in range(4)]
    markerFound = False
    while not markerFound:
        buffer[i % 4] = f.read(1)
        i += 1
        if i >= 4 and len(set(buffer)) == 4:
            markerFound = True

    print(i)