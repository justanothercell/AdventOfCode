for c in range(8):
    for i in range(4):
        if (c+3) % 4 == 3-i:
            print('A', end='')
        if (c+2) % 4 == 3-i:
            print('B', end='')
        if (c+1) % 4 == 3-i:
            print('C', end='')
        if c % 4 == 3-i:
            print('D', end='')
    print()