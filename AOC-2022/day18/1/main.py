with open('input.txt') as infile:
    droplets = infile.readlines()

# open_sides: 58
# droplets = [
#     '2,2,2',
#     '1,2,2',
#     '3,2,2',
#     '2,1,2',
#     '2,3,2',
#     '2,2,1',
#     '2,2,3',
#     '2,2,4',
#     '2,2,6',
#     '1,2,5',
#     '3,2,5',
#     '2,1,5',
#     '2,3,5',
# ]

max_bounds = (0, 0, 0)

for droplet in droplets:
    x, y, z = (int(c) + 1 for c in droplet.strip().split(','))
    if x > max_bounds[0] or y > max_bounds[1] or z > max_bounds[2]:
        px, py, pz = max_bounds
        max_bounds = max(x, px), max(y, py), max(pz, z)

print(f'size: {max_bounds}')

voxels = [[[0 for _ in range(max_bounds[2])] for _ in range(max_bounds[1])] for _ in range(max_bounds[0])]

for droplet in droplets:
    x, y, z = (int(c) for c in droplet.strip().split(','))
    voxels[x][y][z] = 1

# flood fill
# -1 means air is connected to outside
propagators = []
for x in range(max_bounds[0]):
    for y in range(max_bounds[1]):
        for z in range(max_bounds[2]):
            if voxels[x][y][z] == 0:
                if x == 0 or x == max_bounds[0]-1 or y == 0 or y == max_bounds[1]-1 or z == 0 or z == max_bounds[2]-1:
                    voxels[x][y][z] = -1
                    propagators.append((x, y, z))

while len(propagators) > 0:
    x, y, z = propagators.pop()
    new = []
    if x > 0:
        new.append((x - 1, y, z))
    if x < max_bounds[0] - 1:
        new.append((x + 1, y, z))
    if y > 0:
        new.append((x, y - 1, z))
    if y < max_bounds[1] - 1:
        new.append((x, y + 1, z))
    if z > 0:
        new.append((x, y, z - 1))
    if z < max_bounds[2] - 1:
        new.append((x, y, z + 1))
    for coord in new:
        x, y, z = coord
        if voxels[x][y][z] == 0:
            voxels[x][y][z] = -1
            propagators.append(coord)


open_sides = 0
# (testdata) size: (4, 4, 7)
# size: (20, 20, 19)

for x in range(max_bounds[0]):
    for y in range(max_bounds[1]):
        for z in range(max_bounds[2]):
            if voxels[x][y][z] != 1:
                continue
            if x == 0 or voxels[x - 1][y][z] == -1:
                open_sides += 1
            if x == max_bounds[0] - 1 or voxels[x + 1][y][z] == -1:
                open_sides += 1
            if y == 0 or voxels[x][y-1][z] == -1:
                open_sides += 1
            if y == max_bounds[1] - 1 or voxels[x][y + 1][z] == -1:
                open_sides += 1
            if z == 0 or voxels[x][y][z - 1] == -1:
                open_sides += 1
            if z == max_bounds[2] - 1 or voxels[x][y][z + 1] == -1:
                open_sides += 1

print(f'open_sides: {open_sides}')
# open_sides: 2082
