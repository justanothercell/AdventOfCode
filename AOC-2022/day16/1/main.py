with open('input.txt') as infile:
    tunnels = infile.readlines()

# total_flow: 1651
#tunnels = [
#    'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
#    'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
#    'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
#    'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
#    'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
#    'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
#    'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
#    'Valve HH has flow rate=22; tunnel leads to valve GG',
#    'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
#    'Valve JJ has flow rate=21; tunnel leads to valve II',
#]


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



#               pos, time, flow, total_flow
paths_heads = [(['AA'], 0, 0, 0)]
max_v = ['AA'], 0, 0, 0

while len(paths_heads) > 0:
    paths_heads.sort(key=lambda x: x[3])
    pos, time, flow, total_flow = paths_heads.pop()
    if time < 30:
        continued = False
        for dest, dist in valve_paths[pos[-1]].items():
            if dest not in pos:
                paths_heads.append((pos + [dest], min(time + dist + 1, 30), flow + valves[dest].flow, total_flow + flow * min(dist + 1, 30-time)))
                continued = True
        if not continued:
            paths_heads.append((pos, 30, flow, total_flow + flow * (30 - time)))
    else:
        if max_v[3] < total_flow:
            max_v = pos, time, flow, total_flow
            print(*max_v)

# ['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC', 'GG', 'II'] 30 81 1651
# ['AA', 'FC', 'SJ', 'IG', 'EW', 'WC', 'JF', 'FP'] 30 114 1871