program = list(map(int, open('17.txt').read().split(',')))
program.extend([0] * 10000)
program[0] = 2

def interpret_opcode(opcode):
    instruction = opcode % 100
    parameters = opcode // 100

    parameter_mode = [0, 0, 0]
    for idx in range(3):
        parameter_mode[idx] = (parameters % 10)
        parameters = parameters // 10

    return instruction, parameter_mode

# from 17b-simulator
A = 'L,12,L,12,L,6,L,6\n'
B = 'R,8,R,4,L,12\n'
C = 'L,12,L,6,R,12,R,8\n'
main = 'A,B,A,C,B,A,C,B,A,C\n'

inputs = main + A + B + C + 'n\n'
input_idx = 0

ip = 0
rb = 0
while program[ip] != 99:
    opcode = program[ip]
    instruction, parameter_mode = interpret_opcode(opcode)

    if instruction == 1:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]
        elif parameter_mode[0] == 2:
            first_val = program[first_val + rb]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]
        elif parameter_mode[1] == 2:
            second_val = program[second_val + rb]

        result = first_val + second_val
        output_address = program[ip+3]
        if parameter_mode[2] == 2:
            output_address += rb

        program[output_address] = result
        ip += 4
    elif instruction == 2:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]
        elif parameter_mode[0] == 2:
            first_val = program[first_val + rb]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]
        elif parameter_mode[1] == 2:
            second_val = program[second_val + rb]

        result = first_val * second_val
        output_address = program[ip+3]
        if parameter_mode[2] == 2:
            output_address += rb

        program[output_address] = result
        ip += 4
    elif instruction == 3:
        input_value = inputs[input_idx]
        input_value = ord(input_value)
        input_idx += 1
        input_address = program[ip+1]
        if parameter_mode[0] == 2:
            input_address += rb
        program[input_address] = input_value
        ip += 2
    elif instruction == 4:
        output_val = program[ip+1]
        if parameter_mode[0] == 0:
            output_val = program[output_val]
        elif parameter_mode[0] == 2:
            output_val = program[output_val + rb]

        if output_val < 255:
            print(chr(output_val), end='')
        else:
            print(output_val)
        ip += 2
    elif instruction == 5:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]
        elif parameter_mode[0] == 2:
            first_val = program[first_val + rb]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]
        elif parameter_mode[1] == 2:
            second_val = program[second_val + rb]

        if first_val != 0:
            ip = second_val
        else:
            ip += 3
    elif instruction == 6:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]
        elif parameter_mode[0] == 2:
            first_val = program[first_val + rb]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]
        elif parameter_mode[1] == 2:
            second_val = program[second_val + rb]

        if first_val == 0:
            ip = second_val
        else:
            ip += 3
    elif instruction == 7:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]
        elif parameter_mode[0] == 2:
            first_val = program[first_val + rb]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]
        elif parameter_mode[1] == 2:
            second_val = program[second_val + rb]

        output_address = program[ip+3]
        if parameter_mode[2] == 2:
            output_address += rb

        if first_val < second_val:
            program[output_address] = 1
        else:
            program[output_address] = 0
        ip += 4
    elif instruction == 8:
        first_val = program[ip+1]
        if parameter_mode[0] == 0:
            first_val = program[first_val]
        elif parameter_mode[0] == 2:
            first_val = program[first_val + rb]

        second_val = program[ip+2]
        if parameter_mode[1] == 0:
            second_val = program[second_val]
        elif parameter_mode[1] == 2:
            second_val = program[second_val + rb]

        output_address = program[ip+3]
        if parameter_mode[2] == 2:
            output_address += rb

        if first_val == second_val:
            program[output_address] = 1
        else:
            program[output_address] = 0
        ip += 4
    elif instruction == 9:
        val = program[ip+1]
        if parameter_mode[0] == 0:
            val = program[val]
        elif parameter_mode[0] == 2:
            val = program[val + rb]
        rb += val
        ip += 2
