with open('input.txt') as infile:
    numbers = [int(n) for n in infile.read().strip().split('\n')]

def mix(res, num):
    return res ^ num

def prune(res):
    return res % 16777216

def next(num):
    # step 1
    num = prune(mix(num * 64, num))
    # step 2
    num = prune(mix(num // 32, num))
    #step 3
    num = prune(mix(num * 2048, num))
    return num

# n = 123
# print(f'testing with {n=}: {n%10}')
# window = 0
# for i in range(10):
#     nn = next(n)
#     delta = nn % 10 - n % 10
#     window <<= 5
#     window |= abs(delta) | (0b10000 if delta < 0 else 0b00000)
#     window &= 0b1111_1111_1111_1111_1111 # 20 digits = 4 * 5 digits
#     b = f'{window:20b}'
#     print(f'  {i}. n={nn:8}: {nn % 10} ({delta:2}) window: {b[0:5]} {b[5:10]} {b[10:15]} {b[15:20]}')
#     n = nn
# print('-'*20)

print('generating sequences...')
seqs = []
all_wins = set()
for i, num in enumerate(numbers):
    if i % 100 == 0:
        print('.', end='', flush=True)
    n = num
    window = 0
    seq = {}
    for j in range(2000):
        nn = next(n)
        delta = nn % 10 - n % 10
        window <<= 5
        window |= abs(delta) | (0b10000 if delta < 0 else 0b00000)
        window &= 0b1111_1111_1111_1111_1111 # 20 digits = 4 * 5 digits
        n = nn
        if j >= 4: # cant sell before
            if window not in seq: # if it was we would have stopped before and never reached this
                seq[window] = nn % 10
                all_wins.add(window)
    seqs.append(seq)
print()
print(f'detected {len(all_wins)} windows in 2000 iterations over {len(numbers)} inputs')
print('comparing windows...')
max_win = 0
max_profit = 0
for i, window in enumerate(all_wins):
    if i % 1000 == 0:
        if i % 10_000 == 0:
            print('|', end='', flush=True)
        else:
            print('.', end='', flush=True)
    profit = 0
    for seq in seqs:
        if window in seq:
            profit += seq[window]
    if profit > max_profit:
        max_profit = profit
        max_win = window
print('done!')
b = f'{max_win:20b}'
print(f'max_win = {b[0:5]} {b[5:10]} {b[10:15]} {b[15:20]} for {max_profit} bananas')
w0 = ((max_win >> 15) & 0b01111) * (-1 if ((max_win >> 15) & 0b10000) > 0 else 1)
w1 = ((max_win >> 10) & 0b01111) * (-1 if ((max_win >> 10) & 0b10000) > 0 else 1)
w2 = ((max_win >>  5) & 0b01111) * (-1 if ((max_win >>  5) & 0b10000) > 0 else 1)
w3 = ((max_win >>  0) & 0b01111) * (-1 if ((max_win >>  0) & 0b10000) > 0 else 1)
print(f'sequence: {w0:2} {w1:2} {w2:2} {w3:2}')
