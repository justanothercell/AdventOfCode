with open("input.txt") as infile:
    rucksacks = infile.readlines()

# rucksacks = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSLn\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw".split('\n')
# total: 70

def priority(c: str):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


total = 0

for i in range(0, len(rucksacks), 3):
    team = rucksacks[i:i+3]
    a, b, c = team
    for item in a:
        if item in b and item in c:
            total += priority(item)
            break

print(f"total: {total}")  # score: 2650
