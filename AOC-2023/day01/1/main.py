with open('input.txt') as infile:
    lines = infile.readlines()

def to_int_or_none(s):
    try:
        return int(s)
    except:
        return None

print(sum([l[0]*10+l[-1] for l in [[i for i in [to_int_or_none(c) for c in line] if i is not None] for line in lines]]))