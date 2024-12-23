with open('input.txt') as infile:
    links = [c.split('-') for c in infile.read().strip().split('\n')]

lmap = {}

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

cliques = []

for node, peers in lmap.items():
    for clique in cliques:
        if clique.issubset(peers):
            cliques.append(clique | set([node]))
    cliques.append(set([node]))

party = max(cliques, key=lambda c: len(c))
key = ','.join(sorted(party))
print(key)
