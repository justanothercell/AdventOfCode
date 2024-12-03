with open('input.txt') as infile:
    memory = infile.read()

# memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

sum = 0
enabled = True

num1 = ''
num2 = ''
state = 0
kind = 0

print('enabled')

for c in memory:
    match state, kind:
        case 0, _:
            num1 = ''
            num2 = ''
            if c == 'm':
                state = 1
                kind = 0
            elif c == 'd':
                state = 1
                kind = 1
            else:
                state = 0
        case 1, 0:
            if c == 'u':
                state = 2
            else:
                state = 0
        case 2, 0:
            if c == 'l':
                state = 3
            else:
                state = 0
        case 3, 0:
            if c == '(':
                state = 4
            else:
                state = 0
        case 4, 0:
            if c in '0123456789':
                num1 += c
            else:
                if c != ',' or len(num1) == 0:
                    state = 0
                else:
                    state = 5
        case 5, 0:
            if c in '0123456789':
                num2 += c
            else:
                if c != ')' or len(num2) == 0:
                    state = 0
                else:
                    print(f'{num1} * {num2}')
                    if enabled:
                        sum += int(num1) * int(num2)
                    state = 0
        case 1, 1:
            if c == 'o':
                state = 2
            else:
                state = 0
        case 2, 1:
            if c == '(':
                state = 3
            elif c == 'n':
                state = 3
                kind = 2
        case 3, 1:
            if c == ')':
                state = 0
                enabled = True
                print('enabled')
            else:
                state = 0
        case 3, 2:
            if c == '\'':
                state = 4
            else:
                state = 0
        case 4, 2:
            if c == 't':
                state = 5
            else:
                state = 0
        case 5, 2:
            if c == '(':
                state = 6
            else:
                state = 0
        case 6, 2:
            if c == ')':
                state = 0
                enabled = False
                print('disabled')
            else:
                state = 0
        case _:
            assert False, f"Unreachable {state} {kind}"

print(sum)
