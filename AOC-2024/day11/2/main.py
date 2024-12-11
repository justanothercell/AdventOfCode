import math

with open('input.txt') as infile:
    data = infile.read().strip()

stones = [int(s) for s in data.split(' ')]

cache = {} # key: (depth, stone), value: count at depth = 0

steps = 0
hits = 0

def cacher(r: int, stone: int, depth: int) -> int:
    if (depth, stone) not in cache:
        cache[(depth, stone)] = r
    return r

def blink(stone: int, depth) -> int:
    global steps, hits
    steps += 1
    if (depth, stone) in cache:
        hits += 1
        return cache[(depth, stone)]
    if depth == 0:
        return 1
    if stone == 0:
        return cacher(blink(1, depth - 1), stone, depth)
    s = str(stone)
    l = len(s)
    if l % 2 == 0:
        c = 0
        c += blink(int(s[:l//2]), depth - 1)
        c += blink(int(s[l//2:]), depth - 1)
        return cacher(c, stone, depth)
    return cacher(blink(stone * 2024, depth - 1), stone, depth)

count = 0

for stone in stones:
    c = blink(stone, 75)
    print('stone:', stone, c)
    count += c

print(steps, hits)
print(count)
