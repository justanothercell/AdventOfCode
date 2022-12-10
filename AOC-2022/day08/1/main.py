with open('input.txt') as infile:
    map = [row.strip() for row in infile.readlines()]

# visible: 21
#map = [
#    '30373',
#    '25512',
#    '65332',
#    '33549',
#    '35390',
#]

visible = 0


def vis(x, y, xd, yd):
    height = map[y][x]
    x += xd
    y += yd
    while 0 <= x <= len(map[0]) - 1 and 0 <= y <= len(map) - 1:
        if height <= map[y][x]:
            return False
        x += xd
        y += yd
    return True


for x in range(len(map[0])):
    for y in range(len(map)):
        if vis(x, y, 1, 0) or vis(x, y, -1, 0) or vis(x, y, 0, 1) or vis(x, y, 0, -1):
            visible += 1


print('visible:', visible)  # visible: 1832

