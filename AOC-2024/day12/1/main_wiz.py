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
            # we are adding new plots with a perimeter of
            # 4 - 2 * left_or_up_neighbors.
            # joining two regions only happens at that single plot
            # and as such we are not miscalculating
            'perimeter': a['perimeter'] + b['perimeter'],
            # we are only joining same-typed regions (note: is called 'color' in th enormal solution)
            'type': a['type'],
            # arbitrarily choosing one
            'color': a['color']
        }
    )

for y in range(h):
    for x in range(w):
        c = map[y][x]
        perimeter = 4
        if x > 0 and map[y][x-1] == c: # will join left
            perimeter -= 2
        if y > 0 and map[y-1][x] == c: # will join up
            perimeter -= 2
        u.register((x, y), {
            'area': 1,
            'perimeter': perimeter,
            'type': c,
            'color': (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        })
        if x > 0 and map[y][x-1] == c: # join left
            u.join((x-1, y), (x, y))
        if y > 0 and map[y-1][x] == c: # join up
            u.join((x, y-1), (x, y))

    # printing!
    print('\x1b[H', end='')
    for py in range(h):
        for px in range(w):
            c = map[py][px]
            if u.contains((px, py)):
                r, g, b = u[(px, py)][1]['color']
                print(f'\x1b[48;2;{r};{g};{b}m{c} \x1b[0m', end='')
            else:
                print(f'{c} ', end='')
        print()
cost = 0

for item, (parent, data) in u.unions.items():
    if parent is None:
        c = data['area'] * data['perimeter']
        cost += c

print(cost)
