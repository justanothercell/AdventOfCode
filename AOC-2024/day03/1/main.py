with open('input.txt') as infile:
    memory = infile.read()

# memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

sum = 0

num1 = ''
num2 = ''
state = 0

for c in memory:
    match state:
        case 0:
            num1 = ''
            num2 = ''
            if c == 'm':
                state = 1
            else:
                state = 0
        case 1:
            if c == 'u':
                state = 2
            else:
                state = 0
        case 2:
            if c == 'l':
                state = 3
            else:
                state = 0
        case 3:
            if c == '(':
                state = 4
            else:
                state = 0
        case 4:
            if c in '0123456789':
                num1 += c
            else:
                if c != ',' or len(num1) == 0:
                    state = 0
                else:
                    state = 5
        case 5:
            if c in '0123456789':
                num2 += c
            else:
                if c != ')' or len(num2) == 0:
                    state = 0
                else:
                    print(f'{num1} * {num2}')
                    sum += int(num1) * int(num2)
                    state = 0
        case _:
            assert False, "Unreachable"

print(sum)
