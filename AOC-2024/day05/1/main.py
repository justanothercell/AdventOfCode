with open('input.txt') as infile:
    raw_data = infile.read().strip()

raw_rules, raw_updates = raw_data.split('\n\n')

rules_list_raw = raw_rules.strip().split('\n')
updates_list_raw = raw_updates.strip().split('\n')

rules_list = [ [int(r) for r in rule.split('|')] for rule in rules_list_raw ]
updates_list = [ [int(u) for u in update.split(',')] for update in updates_list_raw]

rev_rules = {}

for x, y in rules_list:
    if y not in rev_rules:
        rev_rules[y] = set()
    rev_rules[y].add(x)

middle_sum = 0

for update in updates_list:
    blacklisted = set()
    error = False
    for page in update:
        if page in blacklisted:
            error = True
            r = None
            for rule in rules_list:
                if rule[0] == page:
                    r = rule[1]
            print(f'Update {update} failed at {page} -> {r}')
            break
        if page not in rev_rules:
            continue
        blacklisted |= rev_rules[page] # you may not print x after you already printed y
    if not error:
        print(f'Update {update} passed')
        middle_sum += update[len(update) // 2]
print(middle_sum)
