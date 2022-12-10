with open('input.txt') as infile:
    rucksacks = infile.readlines()

# rucksacks = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSLn\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw".split('\n')
# total: 157

def priority(c: str):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


total = 0

print(rucksacks)

for items in rucksacks:
    left = items[:len(items) // 2]
    right = items[len(items) // 2:]
    for item in right:
        if item in left:
            total += priority(item)
            break

print(f'total: {total}')  # score: 7428
