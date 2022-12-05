with open('input.txt') as infile:
    pairs = infile.readlines()

#pairs = [
#    "2-4,6-8",
#    "2-3,4-5",
#    "5-7,7-9",
#    "2-8,3-7",
#    "6-6,4-6",
#    "2-6,4-8"
#]
# total: 2

total = 0


for pair in pairs:
    left, right = map(lambda r: list(map(int, r.split('-'))), pair.split(','))
    def check(a, b):
        return a[0] >= b[0] and a[1] <= b[1]

    if check(left, right) or check(right, left):
        total += 1


print(f'total: {total}')  # total: 560
