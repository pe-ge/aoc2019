program = list(map(int, open('15.txt').read().split(',')))
program.extend([0] * 10000)

action_to_id = {
    'N': 1,
    'S': 2,
    'W': 3,
    'E': 4
}

opposite_action = {
    'N': 'S',
    'S': 'N',
    'W': 'E',
    'E': 'W',
}

id_to_delta = {
    1: (0, -1),
    2: (0, 1),
    3: (-1, 0),
    4: (1, 0)
}

width = 50
height = 50

world = [[' ' for _ in range(height)] for _ in range(width)]

init_x = width // 2
init_y = height // 2
robot_x = init_x
robot_y = init_y
oxygen_x = 0
oxygen_y = 0
input_value = None

history = list()
backtracking = False

actions = ['N', 'W', 'S', 'E']


def print_world():
    world_robot = world[:]
    world_robot[robot_x][robot_y] = 'D'
    world_robot[oxygen_x][oxygen_y] = 'O'
    for y in range(height):
        for x in range(width):
            print(world_robot[x][y], end='')
        print()

def handle_output(output, input_value):
    global robot_x, robot_y, oxygen_x, oxygen_y
    dx, dy = id_to_delta[input_value]
    if output == 0:
        world[robot_x + dx][robot_y + dy] = '#'
        history.pop()
    elif output == 1:
        world[robot_x][robot_y] = '.'
        robot_x += dx
        robot_y += dy
    elif output == 2:
        world[robot_x][robot_y] = '.'
        robot_x += dx
        robot_y += dy
        oxygen_x = robot_x
        oxygen_y = robot_y
        world[robot_x][robot_y] = 'O'

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
        # first find empty around
        backtracking = True
        for next_action in actions:
            dx, dy = id_to_delta[action_to_id[next_action]]
            if world[robot_x + dx][robot_y + dy] == ' ':
                backtracking = False
                history.append(opposite_action[next_action])
                break

        # if nothing empty around, backtrack
        if backtracking:
            if history:
                next_action = history.pop()
            else:
                break

        input_value = action_to_id[next_action]
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

        handle_output(output_val, input_value)
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


to_visit = [(oxygen_x, oxygen_y, 0)]
while to_visit:
    x, y, d = to_visit.pop(0)
    if world[x][y] not in ('O', 'D', '.'):
        continue
    world[x][y] = 'x'
    to_visit.append((x-1, y, d+1))
    to_visit.append((x+1, y, d+1))
    to_visit.append((x, y-1, d+1))
    to_visit.append((x, y+1, d+1))

print(d-1)
