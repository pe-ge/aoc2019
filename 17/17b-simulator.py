world = list(map(list, open('world.txt').read().split('\n')))

robot_r, robot_c = None, None
robot_o = None
orientations = ['<', '^', '>', 'v']
directions = {
    'L': -1,
    'R': 1
}
movement = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}

for row_idx in range(len(world)):
    for col_idx in range(len(world[row_idx])):
        if world[row_idx][col_idx] in ('^', '<', 'v', '>'):
            robot_r, robot_c = row_idx, col_idx
            robot_o = world[row_idx][col_idx]
            world[row_idx][col_idx] = '#'


def print_world(world, robot_r, robot_c):
    for row_idx in range(len(world)):
        for col_idx in range(len(world[row_idx])):
            if row_idx == robot_r and col_idx == robot_c:
                print(robot_o, end='')
            else:
                print(world[row_idx][col_idx], end='')
        print()
    print()

def rotate(robot_o, direction):
    do = directions[direction]
    robot_o = orientations[(orientations.index(robot_o) + do) % len(orientations)]
    return robot_o

def execute(world, robot_r, robot_c, robot_o, cmd):
    instructions = cmd.split(',')
    for instruction in instructions:
        if instruction in ('L', 'R'):
            robot_o = rotate(robot_o, instruction)
        else:
            num_steps = int(instruction)
            dr, dc = movement[robot_o]
            robot_r += dr * num_steps
            robot_c += dc * num_steps

    return robot_r, robot_c, robot_o

# manually found functions
A = 'L,12,L,12,L,6,L,6'
B = 'R,8,R,4,L,12'
C = 'L,12,L,6,R,12,R,8'
cmd = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (A,B,A,C,B,A,C,B,A,C)
robot_r, robot_c, robot_o = execute(world, robot_r, robot_c, robot_o, cmd)
print_world(world, robot_r, robot_c)
