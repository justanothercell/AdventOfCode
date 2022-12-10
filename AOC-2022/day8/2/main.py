with open('input.txt') as infile:
    map = [row.strip() for row in infile.readlines()]

# max_score: 8
#map = [
#    '30373',
#    '25512',
#    '65332',
#    '33549',
#    '35390',
#]

max_score = 0


def vis(x, y, xd, yd):
    height = map[y][x]
    x += xd
    y += yd
    score = 0
    while 0 <= x <= len(map[0]) - 1 and 0 <= y <= len(map) - 1:
        score += 1
        if height <= map[y][x]:
            return score
        x += xd
        y += yd
    return score


for x in range(len(map[0])):
    for y in range(len(map)):
        score = vis(x, y, 1, 0) * vis(x, y, -1, 0) * vis(x, y, 0, 1) * vis(x, y, 0, -1)
        max_score = max(max_score, score)


print('max_score:', max_score)  # max_score: 157320
