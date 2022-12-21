with open('input.txt') as infile:
    blueprints_text = infile.readlines()[0].strip()

# quality_levels: [9, 24]
# sum: 33

blueprints_text = [
  'Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.',
  'Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'
]


blueprints = []

for bpt in blueprints_text:
    _, _, _, _, ore_rbt, _, \
    _, _, _, _, clay_rbt, _, \
    _, _, _, _, obby_rbt_ore, _, _, obby_rbt_clay, _,\
    _, _, _, _, geode_rbt_ore, _, _, geode_rbt_obby, _ = bpt.strip().split()
    blueprints.append((ore_rbt, clay_rbt, (obby_rbt_ore, obby_rbt_clay), (geode_rbt_ore, geode_rbt_obby)))
    print(blueprints[-1])