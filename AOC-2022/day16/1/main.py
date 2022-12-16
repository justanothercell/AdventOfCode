with open('input.txt') as infile:
    tunnels = infile.readlines()

# total_flow: 1651
tunnels = [
    'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
    'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
    'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
    'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
    'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
    'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
    'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
    'Valve HH has flow rate=22; tunnel leads to valve GG',
    'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
    'Valve JJ has flow rate=21; tunnel leads to valve II',
]


class Valve:
    def __init__(self, flow, conns):
        self.flow = flow
        self.conns = conns
        self.open = False


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

for k, p in valve_paths.items():
    print(k, p)


flow = 0
total_flow = 0
time = 1

def goto(v):
    global flow, total_flow, time
    time += 1
    if time >= 30:
        return
    valve = valves[v]
    if not valve.open:
        valve.open = True
        flow += valve.flow
    min_v = '', 10000000000000
    for dest, d in valve_paths[v].items():
        if not valves[dest].open and d < min_v[1] * flow + valves[dest].flow:
            min_v = dest, d
    if min_v[0] != '':
        total_flow += min_v[1]
        goto(min_v[0])


goto('AA')


print(f'flow: {flow}')
print(f'total_flow: {total_flow}')
