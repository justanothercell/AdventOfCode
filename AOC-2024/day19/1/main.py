with open('input.txt') as infile:
    raw_towels, raw_patters = infile.read().strip().split('\n\n')

towels = raw_towels.split(', ')
patterns = raw_patters.split('\n')

possible = 0

def test(pattern):
    for towel in towels:
        if towel == pattern:
            return towel
        if pattern.startswith(towel):
            r = test(pattern[len(towel):])
            if r is not None:
                return towel + ' ' + r
    return None
for i, pattern in enumerate(patterns):
    r = test(pattern)
    if r is not None:
        print(r)
        possible += 1
print(f'managed to produce {possible} patters out of {len(patterns)}')
