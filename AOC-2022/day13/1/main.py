with open('input.txt') as infile:
    packets = infile.readlines()

# right_order: [1, 2, 4, 6]
# sum: 13
# packets = [
#     '[1,1,3,1,1]',
#     '[1,1,5,1,1]',
#     '',
#     '[[1],[2,3,4]]',
#     '[[1],4]',
#     '',
#     '[9]',
#     '[[8,7,6]]',
#     '',
#     '[[4,4],4,4]',
#     '[[4,4],4,4,4]',
#     '',
#     '[7,7,7,7]',
#     '[7,7,7]',
#     '',
#     '[]',
#     '[3]',
#     '',
#     '[[[]]]',
#     '[[]]',
#     '',
#     '[1,[2,[3,[4,[5,6,7]]]],8,9]',
#     '[1,[2,[3,[4,[5,6,0]]]],8,9]',
# ]


#  1: "verified"
# -1: "verified wrong"
#  0: "equal"
def comp(l, r):
    print(l)
    print(r)
    print()
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return 1
        if l > r:
            return -1
        return 0
    if isinstance(l, list) and isinstance(r, int):
        return comp(l, [r])
    if isinstance(l, int) and isinstance(r, list):
        return comp([l], r)
    if isinstance(l, list) and isinstance(r, list):
        for i in range(min(len(l), len(r))):
            print(f'[{i}/{min(len(l), len(r))}]: {l[i]}')
            print(f'[{i}/{min(len(l), len(r))}]: {r[i]}')
            c = comp(l[i], r[i])
            print(f'[{i}/{min(len(l), len(r))}]> {c}')
            if c != 0:
                return c
        if len(l) < len(r):
            return 1
        if len(l) > len(r):
            return -1
        return 0


right_order = []

for i in range(len(packets) // 3):
    left, right, _ = packets[i*3:i*3+3]
    left = eval(left.strip())
    right = eval(right.strip())
    c = comp(left, right)
    if c == 1:
        right_order.append(i + 1)
    print(f'=> {c}')
    print('==================')
    print()

print(f'right_order: {right_order}')
print(f'sum: {sum(right_order)}')

# right_order: [1, 2, 4, 5, 8, 10, 12, 13, 14, 17, 18, 21, 24, 25, 28, 29, 31, 32, 34, 35, 36, 37, 39, 40, 44, 47, 52, 53, 54, 56, 57, 58, 60, 62, 63, 64, 65, 67, 69, 70, 71, 72, 76, 77, 78, 81, 84, 87, 90, 91, 92, 94, 95, 99, 100, 103, 106, 108, 111, 112, 113, 115, 116, 121, 123, 124, 127, 130, 136, 138, 139, 142, 143, 146, 148, 149]
# sum: 5393
