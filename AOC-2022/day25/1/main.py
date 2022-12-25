with open('input.txt') as infile:
    snafus = [l.rstrip() for l in infile.readlines()]

# snafus = [
#     '1=-0-2',
#     '12111',
#     '2=0=',
#     '21',
#     '2=01',
#     '111',
#     '20012',
#     '112',
#     '1=-1=',
#     '1-12',
#     '12',
#     '1=',
#     '122',
# ]


def base5(n):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % 5))
        n //= 5
    return ''.join(digits[::-1])

#  snafu    dec  base5
# 1=-0-2   1747  23442
#  12111    906  12111
#   2=0=    198   1243
#     21     11     21
#   2=01    201   1301
#    111     31    111
#  20012   1257  20012
#    112     32    112
#  1=-1=    353   2403
#   1-12    107    412
#     12      7     12
#     1=      3      3
#    122     37    122
# total: 4890
# snafu: 2=-1=0

def snafu_dec(s):
    n = 0
    for i, c in enumerate(s[::-1]):
        match c:
            case '2':
                n += 5 ** i * 2
            case '1':
                n += 5 ** i
            case '0':
                pass
            case '-':
                n -= 5 ** i
            case '=':
                n -= 5 ** i * 2
    return n


def dec_snafu(n):
    b5 = [int(x) for x in base5(n)][::-1] + [0]
    s = ''
    for i, b in enumerate(b5):
        if b >= 5:
            b -= 5
            b5[i+1] += 1
        if b <= 2:
            s += str(b)
        else:
            if b == 3:
                s += '='
            else:
                s += '-'
            b5[i + 1] += 1

    return s[::-1].lstrip('0')


ints = []

print(' input    dec  base5  snafu')
for snafu in snafus:
    n = snafu_dec(snafu)
    ints.append(n)
    print(f'{snafu:>6} {n:>6} {base5(n):>6} {dec_snafu(n):>6}')


total = sum(ints)
print(f'total: {total}')
print(f'snafu: {dec_snafu(total)}')
# total: 33010101016442
# snafu: 2-=12=2-2-2-=0012==2
