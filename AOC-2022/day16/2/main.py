from itertools import permutations
from math import factorial

with open('input.txt') as infile:
    tunnels = infile.readlines()

# total_flow: (['JJ', 'BB', 'CC'], ['DD', 'HH', 'EE'], 81, 1707)
# tunnels = [
#     'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
#     'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
#     'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
#     'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
#     'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
#     'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
#     'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
#     'Valve HH has flow rate=22; tunnel leads to valve GG',
#     'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
#     'Valve JJ has flow rate=21; tunnel leads to valve II',
# ]


class Valve:
    def __init__(self, flow, conns):
        self.flow = flow
        self.conns = conns


valves = {}


for tunnel in tunnels:
    _, valve, _, _, rate, _, _, _, _, *conns = tunnel.strip().split()
    flow = int(rate[5:-1])
    valves[valve] = Valve(flow, [c.rstrip(',') for c in conns])


valve_paths = {}


def apply_connection(start, end, length):
    if end not in valve_paths[start] or valve_paths[start][end] > length:
        valve_paths[start][end] = length
        for c in valves[end].conns:
            apply_connection(start, c, length + 1)


for (name, valve) in valves.items():
    valve_paths[name] = {}
    for c in valve.conns:
        apply_connection(name, c, 1)


for k in valve_paths.keys():
    for kk in list(valve_paths[k].keys()):
        if valves[kk].flow == 0:
            valve_paths[k].pop(kk)


for k, p in valve_paths.items():
    print(k, p)
print()

# test data solution order:
# tasks = ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']  # removed the leading 'AA'
# real data solution oder:
# tasks = ['FC', 'SJ', 'IG', 'EW', 'WC', 'JF', 'FP']  # removed the leading 'AA'

# test evaluation:
# moves as explained by example, square brackets means "opens":
# alone:
#   me: AA [DD] [BB] II [JJ] II AA DD EE FF GG [HH] GG FF [EE] DD [CC]
#     condensed: AA DD BB JJ HH EE CC
# together:
#   me: AA II [JJ] II AA [BB] [CC]
#     condensed: AA JJ BB CC
#   elephant: AA [DD] EE FF GG HH [HH] GG FF [EE]
#     condensed: AA DD HH EE
# elephant and me distribute tasks evenly


tasks = valve_paths['AA'].keys()


def simulate(m_tasks, e_tasks):
    m_pos = 'AA'
    m_d = 0
    m_path = []

    e_pos = 'AA'
    e_d = 0
    e_path = []

    flow = 0
    total_flow = 0
    time = 0

    while time < 26:
        if len(m_tasks) > 0:
            if m_d == 0:
                flow += valves[m_pos].flow
                dest = m_tasks.pop(0)
                m_d = valve_paths[m_pos][dest] + 1
                m_pos = dest
                m_path.append(dest)
        else:
            if m_d == 0:
                flow += valves[m_pos].flow
        if len(e_tasks) > 0:
            if e_d == 0:
                flow += valves[e_pos].flow
                dest = e_tasks.pop(0)
                e_d = valve_paths[e_pos][dest] + 1
                e_pos = dest
                e_path.append(dest)
        else:
            if e_d == 0:
                flow += valves[e_pos].flow
        m_d -= 1
        e_d -= 1
        total_flow += flow
        time += 1
    return m_path, e_path, flow, total_flow


total = factorial(len(tasks))
d = total // 10000000

highest = (None, None, 0, 0)

for i, order in enumerate(permutations(tasks)):
    mp, ep, f, ft = simulate(list(order[len(order)//2:]), list(order[:len(order)//2]))
    if ft > highest[3]:
        highest = mp, ep, f, ft
        print(highest)
    if i % d == 0:
        print(i / total)

print()
print(highest)