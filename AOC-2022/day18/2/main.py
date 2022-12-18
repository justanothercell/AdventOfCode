with open('input.txt') as infile:
    droplets = infile.readlines()

# open_sides: 64
#droplets = [
#    '2,2,2',
#    '1,2,2',
#    '3,2,2',
#    '2,1,2',
#    '2,3,2',
#    '2,2,1',
#    '2,2,3',
#    '2,2,4',
#    '2,2,6',
#    '1,2,5',
#    '3,2,5',
#    '2,1,5',
#    '2,3,5',
#]

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

open_sides = 0
# size: (20, 20, 19)

for x in range(max_bounds[0]):
    for y in range(max_bounds[1]):
        for z in range(max_bounds[2]):
            if voxels[x][y][z] == 0:
                continue
            if x == 0 or voxels[x-1][y][z] == 0:
                open_sides += 1
            if x == max_bounds[0] - 1 or voxels[x+1][y][z] == 0:
                open_sides += 1
            if y == 0 or voxels[x][y-1][z] == 0:
                open_sides += 1
            if y == max_bounds[1] - 1 or voxels[x][y+1][z] == 0:
                open_sides += 1
            if z == 0 or voxels[x][y][z-1] == 0:
                open_sides += 1
            if z == max_bounds[2] - 1 or voxels[x][y][z+1] == 0:
                open_sides += 1

print(f'open_sides: {open_sides}')
# open_sides: 3610
