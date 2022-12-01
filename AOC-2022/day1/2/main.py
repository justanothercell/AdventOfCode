with open("input.txt") as infile:
    input_calories = infile.readlines()

max_counts = []

current_count = 0

for line in input_calories:
    if len(line.strip()) == 0:
        max_counts.append(current_count)
        max_counts.sort()
        max_counts = max_counts[-3:]
        current_count = 0
    else:
        current_count += int(line.strip())

print(f"max 3: {max_counts}")  # max 3: [66250, 66306, 66616]
print(f"sum(max 3): {sum(max_counts)}")  # max 3: [66250, 66306, 66616]

