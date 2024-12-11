import math

with open('input.txt') as infile:
    data = infile.read().strip()

stones = [int(s) for s in data.split(' ')]

cache = {} # key: (depth, stone), value: count at depth = 0

def blink(stone: int, depth) -> int:
    if depth == 0:
        return 1
    if (depth, stone) in cache:
        return cache[(depth, stone)]
    if stone == 0:
        r = blink(1, depth - 1)
        cache[(depth, stone)] = r
        return r
    l = int(math.log10(stone)) + 1
    l10 = 10**(l//2)
    if l % 2 == 0:
        r = blink(stone // l10, depth - 1) + blink(stone % l10, depth - 1)
        cache[(depth, stone)] = r
        return r
    r = blink(stone * 2024, depth - 1)
    cache[(depth, stone)] = r
    return r

count = 0

for stone in stones:
    count += blink(stone, 75)

print(count)
