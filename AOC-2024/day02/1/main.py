with open('input.txt') as infile:
    raw_data = infile.readlines()

data = []

for row in raw_data:
    row = row.strip()
    if len(row) > 0:
        data.append([int(x) for x in row.split()])

safe = 0

for report in data:
    if len(report) < 2:
        safe += 1
        continue
    up = report[0] < report[1]
    is_safe = True
    for i in range(len(report) - 1):
        if report[i] == report[i+1]: # is unsafe
            is_safe = False
            break
        if (report[i] < report[i+1]) != up: # wrong direction
            is_safe = False
            break
        delta = abs(report[i+1] - report[i])
        if delta > 3: # also unsafe
            is_safe = False
            break
    if is_safe:
        safe += 1
print(safe)
