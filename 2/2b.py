def execute(program, noun, verb):
    program[1] = noun
    program[2] = verb

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

    return program[0]

program = list(map(int, open('2.txt').read().split(',')))
for noun in range(100):
    for verb in range(100):
        program_copied = program[:]
        result = execute(program_copied, noun, verb)
        if result == 19690720:
            print(100 * noun + verb)
