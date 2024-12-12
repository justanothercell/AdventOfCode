import random

class UnionFind:
    def __init__(self, f_join):
        self.unions = {}
        self.f_join = f_join

    def __getitem__(self, item): # find representative of the class of item
        items = []
        data = None
        assert item in self.unions, f'Item {item} not registered yet'
        while True: # we are not root yet
            parent, data = self.unions[item]
            if parent is None:
                assert data is not None
                break
            else:
                items.append(item)
            item = parent
        for i in items: # simplify
            self.unions[i] = item, None # setting direct root
        return item, data

    def register(self, item, data):
        self.unions[item] = None, data

    def contains(self, item) -> bool:
        return item in self.unions

    def join(self, a, b): # unite the two classes a and b belong to
        root_a, data_a = self[a]
        root_b, data_b = self[b]
        if data_a is data_b: # a and b are already in the same class
            return
        data = self.f_join(data_a, data_b)
        self.unions[root_b] = root_a, None # root_a is now the root of both and root_b is no longer a root
        self.unions[root_a] = None, data
        return root_b, data

with open('input.txt') as infile:
    map = infile.read().strip().split('\n')

w, h = len(map[0]), len(map)

u = UnionFind(
        lambda a, b: {
            # area adds up trivially
            'area': a['area'] + b['area'],
            'corners': a['corners'] ^ b['corners'],
            # arbitrarily choosing one
            'color': a['color'],
            # we are only joining same-typed regions
            'type': a['type']
        }
    )

for y in range(h):
    for x in range(w):
        c = map[y][x]
        joining1 = False
        joining2 = False
        new = [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]
        if x > 0 and map[y][x-1] == c:
            joining1 = True
        if y > 0 and map[y-1][x] == c:
            joining1 = True
            joining2 = True
        if x < w-1 and map[y][x+1] == c:
            joining2 = True
        # offset corners so they dont overlap when they dont actually join anything.
        # try small_input_2.txt wihout this (visualizing "A") to see why this is important
        if not joining1: # edge/corner case
            new[0] = (x+0.1, y+0.1)
        if not joining2: # edge/corner case
            new[1] = (x+1.05, y+0.05)
        u.register((x, y), {
            'area': 1,
            'corners': set(new),
            'color': (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)),
            'type': c
        })
        if x > 0 and map[y][x-1] == c: # join left
            u.join((x, y), (x-1, y))
        if y > 0 and map[y-1][x] == c: # join up
            u.join((x, y), (x, y-1))

cost = 0
all = set()

for item, (parent, data) in u.unions.items():
    if parent is None:
        all |= data['corners']
        c = data['area'] * len(data['corners'])
        cost += c
        print(f'type: {data["type"]}\tarea: {data["area"]:5}\tedges: {len(data["corners"]):5}\tcost: {c:5}')

print(cost)

print()

all = set()
#                                                                                         v select which letters to display
for c in [i[1][1]['corners'] for i in u.unions.items() if i[1][1] and i[1][1]['type'] in 'RI']:
    #           remove offset for displaying, corners may overlap here
    all |= set([(int(x), int(y)) for x, y in c])

for y in range(h):
    fx = False
    for x in range(min(w + 1, 80)):
        if (x, y) in all:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
    for x in range(min(w, 80)):
        r, g, b = u[(x, y)][1]['color']
        print(f' \x1b[48;2;{r};{g};{b}m{map[y][x]}\x1b[0m', end='')
    print()
for x in range(min(w + 1, 80)):
    if (x, h) in all:
        print('* ', end='')
    else:
        print('  ', end='')
print()

