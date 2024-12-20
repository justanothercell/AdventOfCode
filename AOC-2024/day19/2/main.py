with open('input.txt') as infile:
    raw_towels, raw_patters = infile.read().strip().split('\n\n')

towels = raw_towels.split(', ')
patterns = raw_patters.split('\n')

possible = 0
cache ={}
def test(pattern):
    if pattern in cache:
        return cache[pattern]
    c = 0
    for towel in towels:
        if towel == pattern:
            c += 1
        if pattern.startswith(towel):
            c += test(pattern[len(towel):])
    cache[pattern] = c
    return c
for i, pattern in enumerate(patterns):
    print('.', end='', flush=True)
    possible += test(pattern)
print()
print(f'managed to produce {possible} pattern combinations from {len(patterns)} patterns')
