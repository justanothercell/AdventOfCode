with open("input.txt") as infile:
    input_calories = infile.readlines()

max_count = 0

current_count = 0

for line in input_calories:
    if len(line.strip()) == 0:
        max_count = max(max_count, current_count)
        current_count = 0
    else:
        current_count += int(line.strip())

print(f"max: {max_count}")  # max: 66616

