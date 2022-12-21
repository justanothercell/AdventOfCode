with open('input.txt') as infile:
    mix_list = infile.readlines()

# x, y, z:  4 -3 2
# coordinate: 3
# mix_list = [
#     '1',
#     '2',
#     '-3',
#     '3',
#     '-2',
#     '0',
#     '4'
# ]

mix_list = [(index, int(i.strip())) for index, i in enumerate(mix_list)]

print([m[1] for m in mix_list])
for i in range(len(mix_list)):
    for j in range(len(mix_list)):
        if mix_list[j][0] == i:
            index, e = mix_list.pop(j)
            mix_list.insert((j + e + len(mix_list)) % len(mix_list), (-1, e))
            break

print([m[1] for m in mix_list])

print()

zero = 0
for i in range(len(mix_list)):
    if mix_list[i][1] == 0:
        zero = i
        break

x = mix_list[(1000 + zero) % len(mix_list)][1]
y = mix_list[(2000 + zero) % len(mix_list)][1]
z = mix_list[(3000 + zero) % len(mix_list)][1]

print('x, y, z: ', x, y, z)
print(f'coordinate: {x+y+z}')
# x, y, z:  -8003 4382 4609
# coordinate: 988