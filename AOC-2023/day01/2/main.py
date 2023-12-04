from itertools import accumulate

with open('input.txt') as infile:
    lines = infile.readlines()

def to_int_or_none(s):
    try:
        return int(s)
    except:
        return None

digits = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'eight': 8, 'nine': 9 }

print(sum([l[0]*10+l[-1] for l in [[i for i in [to_int_or_none(c) for c in list(accumulate(range(len(lines[1])-5), lambda line, i: list(accumulate(digits.items(), lambda line, r: line[:i]+line[i:i+5].replace(r[0], str(r[1]))+line[i+5:], initial=line))[-1], initial=line))[-1]] if i is not None] for line in lines]]))