program = list(map(int, open('5.txt').read().split(',')))
input_value = 5
output_address = None

def interpret_opcode(opcode):
    instruction = opcode % 100
    parameters = opcode // 100

    parameter_mode = [0, 0, 0]
    for idx in range(3):
        parameter_mode[idx] = (parameters % 10)
        parameters = parameters // 10

    return instruction, parameter_mode

ip = 0
while program[ip] != 99:
    opcode = program[ip]
    instruction, parameter_mode = interpret_opcode(opcode)

    if instruction == 1:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]

        result = first_val + second_val
        program[program[ip+3]] = result
        ip += 4
    elif instruction == 2:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]

        result = first_val * second_val
        program[program[ip+3]] = result
        ip += 4
    elif instruction == 3:
        input_address = program[ip+1]
        program[input_address] = input_value
        ip += 2
    elif instruction == 4:
        output_address = program[ip+1]
        ip += 2
    elif instruction == 5:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]

        if first_val != 0:
            ip = second_val
        else:
            ip += 3
    elif instruction == 6:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]

        if first_val == 0:
            ip = second_val
        else:
            ip += 3
    elif instruction == 7:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]

        if first_val < second_val:
            program[program[ip+3]] = 1
        else:
            program[program[ip+3]] = 0
        ip += 4
    elif instruction == 8:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]

        if first_val == second_val:
            program[program[ip+3]] = 1
        else:
            program[program[ip+3]] = 0
        ip += 4

print(program[output_address])
