from typing import Union

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
    print(valve, flow, [c.rstrip(',') for c in conns])

print()
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
print()

flow = 0
flows = []
time = 0

flows.append(flow)

def goto(v):
    global flow, flows, time
    time += 1
    flows.append(flow)
    print(v, time, flow, end='')
    if time >= 30:
        return
    valve = valves[v]
    if not valve.open:
        valve.open = True
        flow += valve.flow
        time += 1
    print(' ->', flow)
    new = '', 0, 0, 0
    for dest, d in valve_paths[v].items():
        v = valves[dest].flow * (30-time-d) + (30-time)*flow
        if not valves[dest].open and new[1] < v:
            new = dest, v, valves[dest].flow, d
    if new[0] != '':
        for i in range(new[3]):
            if i + time > 30:
                return
            flows.append(flow)
        time += new[3]
        goto(new[0])


goto('AA')


print(f'flow: {flow}')
print(f'flows: {flows}')
print(f'total_flow: {sum(flows)}')
