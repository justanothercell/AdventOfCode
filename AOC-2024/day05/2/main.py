with open('input.txt') as infile:
    raw_data = infile.read().strip()

raw_rules, raw_updates = raw_data.split('\n\n')

rules_list_raw = raw_rules.strip().split('\n')
updates_list_raw = raw_updates.strip().split('\n')

rules_list = [ [int(r) for r in rule.split('|')] for rule in rules_list_raw ]
updates_list = [ [int(u) for u in update.split(',')] for update in updates_list_raw]

# rules:     x|y -> x has to be printed before y
# rev_rules: y|X -> once y is printed any in X may no longer be printed

rev_rules = {}

for x, y in rules_list:
    if y not in rev_rules:
        rev_rules[y] = set()
    rev_rules[y].add(x)

middle_sum = 0

for update in updates_list:
    error = False
    i = 0
    while i < len(update):
        page = update[i]
        if page not in rev_rules:
            i += 1
            continue
        blacklisted = rev_rules[page] # you may not print any of X after you already printed y
        for j in range(i + 1, len(update)):
            pp = update[j]
            if pp in blacklisted:
                error = True
                print(f'Update {update} contains error at {page} -> {pp}, swapping')
                update[i], update[j] = update[j], update[i]
                print(f'-> {update}')
                i = 0
                break
        else:
            i += 1
    if error:
        print(f'Update {update} fixed and added')
        middle_sum += update[len(update) // 2]
    else:
        print(f'Update {update} passed')

print(middle_sum)
