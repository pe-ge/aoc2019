program = list(map(int, open('2.txt').read().split(',')))
program[1] = 12
program[2] = 2

ip = 0
while program[ip] != 99:
    opcode = program[ip]
    first_val = program[program[ip+1]]
    second_val = program[program[ip+2]]
    if opcode == 1:
        result = first_val + second_val
    else:
        result = first_val * second_val

    program[program[ip+3]] = result
    ip += 4

print(program[0])
