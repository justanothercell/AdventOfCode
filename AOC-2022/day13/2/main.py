from functools import cmp_to_key

with open('input.txt') as infile:
    packets = infile.readlines()

# divider 1: 10
# divider 2: 14
# decoder key: 140
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

packets += ['[[2]]', '[[6]]']

pkts = packets
packets = []

for p in pkts:
    if len(p.strip()) > 0:
        packets.append(eval(p.strip()))


#  1: "verified"
# -1: "verified wrong"
#  0: "equal"
def comp(l, r):
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
            c = comp(l[i], r[i])
            if c != 0:
                return c
        if len(l) < len(r):
            return 1
        if len(l) > len(r):
            return -1
        return 0


sorted_packets = sorted(packets, key=cmp_to_key(lambda l, r: -comp(l, r)))

print('ordered packets:')
for p in sorted_packets:
    print(p)

print()

divider_1 = sorted_packets.index([[2]]) + 1
divider_2 = sorted_packets.index([[6]]) + 1

print(f'divider 1: {divider_1}')
print(f'divider 2: {divider_2}')
print(f'decoder key: {divider_1 * divider_2}')

# divider 1: 126
# divider 2: 212
# decoder key: 26712
