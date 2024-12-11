import math

with open('input.txt') as infile:
    data = infile.read().strip()

stones = [int(s) for s in data.split(' ')]

out_stones = []

def blink(stone: int, out: list[int], depth):
    if depth == 0:
        out.append(stone)
        return
    if stone == 0:
        blink(1, out, depth - 1)
        return
    s = str(stone)
    l = len(s)
    if l % 2 == 0:
        blink(int(s[:l//2]), out, depth - 1)
        blink(int(s[l//2:]), out, depth - 1)
        return
    blink(stone * 2024, out, depth - 1)

for stone in stones:
    blink(stone, out_stones, 25)

print(len(out_stones))
