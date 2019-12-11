program = list(map(int, open('11.txt').read().split(',')))
program.extend([0] * 10000)

world_size = 100
world = [['.'] * world_size for _ in range(world_size)]
robot_row = world_size // 2
robot_col = world_size // 2
all_orientations = ['<', '^', '>', 'v']
robot_orientation = '^'
first_output = True
robot_positions = set([(robot_row, robot_col)])

def turn_left():
    return all_orientations[(all_orientations.index(robot_orientation) - 1) % len(all_orientations)]

def turn_right():
    return all_orientations[(all_orientations.index(robot_orientation) + 1) % len(all_orientations)]

def move_robot():
    if robot_orientation == '^':
        return robot_row - 1, robot_col
    elif robot_orientation == 'v':
        return robot_row + 1, robot_col
    elif robot_orientation == '<':
        return robot_row, robot_col - 1
    elif robot_orientation == '>':
        return robot_row, robot_col + 1

def print_world():
    for row in world:
        print(row)
    print()

def interpret_opcode(opcode):
    instruction = opcode % 100
    parameters = opcode // 100

    parameter_mode = [0, 0, 0]
    for idx in range(3):
        parameter_mode[idx] = (parameters % 10)
        parameters = parameters // 10

    return instruction, parameter_mode

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
        input_address = program[ip+1]
        if parameter_mode[0] == 2:
            input_address += rb

        input_value = 0 if world[robot_row][robot_col] == '.' else 1
        program[input_address] = input_value
        ip += 2
    elif instruction == 4:
        output_val = program[ip+1]
        if parameter_mode[0] == 0:
            output_val = program[output_val]
        elif parameter_mode[0] == 2:
            output_val = program[output_val + rb]

        if first_output:
            world[robot_row][robot_col] = '.' if output_val == 0 else '#'
            # print_world()
        else:
            if output_val == 0:
                robot_orientation = turn_left()
            else:
                robot_orientation = turn_right()

            robot_row, robot_col = move_robot()
            # print(robot_row, robot_col)
            robot_positions.add((robot_row, robot_col))

        first_output = not first_output
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

print(len(robot_positions))
