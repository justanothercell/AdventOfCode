with open('input.txt') as infile:
    raw_regs, raw_program = infile.read().strip().split('\n\n')

orig_a, orig_b, orig_c = [int(r.split(': ')[1]) for r in raw_regs.split('\n')]

program = [int(x) for x in raw_program.split(': ')[1].split(',')]

OP_ADV = 0 # a = a // 2**val(imm)
OP_BXL = 1 # b = b ^ imm
OP_BST = 2 # b = val(imm) % 8
OP_JNZ = 3 # if a != 0: pc = imm
OP_BXC = 4 # b = b ^ c
OP_OUT = 5 # print(val(imm))
OP_BDV = 6 # b = a // 2**val(imm)
OP_CDV = 7 # c = a // 2**val(imm)

def val(imm):
    if 0 <= imm < 4:
        return imm
    if imm == 4:
        return a
    if imm == 5:
        return b
    if imm == 6:
        return c
    assert False, f'invalid combo immediate: {imm}'

orig_a = 0
max = 0
max_a = 0

while True:
    a, b, c = orig_a, orig_b, orig_c
    pc = 0
    orig_a += 1
    if orig_a % 10_000 == 0:
        print(f'{orig_a}')
    printdex = 0
    first_print = False
    while pc < len(program):
        instr = program[pc]
        imm = program[pc+1]
        pc += 2
        if instr == OP_ADV:
            a = a // 2**val(imm)
        elif instr == OP_BXL:
            b = b ^ imm
        elif instr == OP_BST:
            b = val(imm) % 8
        elif instr == OP_JNZ:
            if a != 0:
                pc = imm
        elif instr == OP_BXC:
            b = b ^ c
        elif instr == OP_OUT:
            v = val(imm) % 8
            if printdex < len(program) and program[printdex] == v:
                printdex += 1
            else:
                success = False
                break
        elif instr == OP_BDV:
            b = a // 2**val(imm)
        elif instr == OP_CDV:
            c = a // 2**val(imm)
        else:
            assert False, f'invalid opcode: {instr}'
    if printdex > max:
        max = printdex
        max_a = orig_a-1
    if printdex == len(program):
        print(f'{orig_a-1}')
        break
