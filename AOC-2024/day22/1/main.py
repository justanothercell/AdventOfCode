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
# print(f'testing with {n=}')
# for i in range(10):
#     n = next(n)
#     print(f'  {i}. {n=}')
#
# print('-'*20)

print('running for 2000 iterations:')
sum = 0
for i, num in enumerate(numbers):
    n = num
    for _ in range(2000):
        n = next(n)
    print(f' #{i}: {num:8} -> {n:8}')
    sum += n

print(f'{sum=}')
