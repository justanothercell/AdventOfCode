with open('input.txt') as infile:
    links = [c.split('-') for c in infile.read().strip().split('\n')]

lmap = {}
trigcount = 0

for a, b in links:
    if a not in lmap:
        lmap[a] = set([b])
    else:
        lmap[a].add(b)
    if b not in lmap:
        lmap[b] = set([a])
    else:
        lmap[b].add(a)
    trig = lmap[a] & lmap[b]
    for t in trig:
        if a[0] == 't' or b[0] == 't' or t[0] == 't':
            trigcount += 1

print(trigcount)
