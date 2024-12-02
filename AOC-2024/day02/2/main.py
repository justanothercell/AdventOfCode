with open('input.txt') as infile:
    raw_data = infile.readlines()

data = []

for row in raw_data:
    row = row.strip()
    if len(row) > 0:
        data.append([int(x) for x in row.split()])

safe = 0

for report in data:
    for j in range(len(report)):
        rep = [x for k, x in enumerate(report) if k != j]
        if len(rep) < 2:
            safe += 1
            break
        up = rep[0] < rep[1]
        is_safe = True
        for i in range(len(rep) - 1):
            if rep[i] == rep[i+1]: # is unsafe
                is_safe = False
                break
            if (rep[i] < rep[i+1]) != up: # wrong direction
                is_safe = False
                break
            delta = abs(rep[i+1] - rep[i])
            if delta > 3: # also unsafe
                is_safe = False
                break
        if is_safe:
            safe += 1
            break
print(safe)
