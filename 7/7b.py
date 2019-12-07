from itertools import permutations

finished = False
class Program:
    def __init__(self, amp_id, program, input_buffer, output_buffer):
        self.amp_id = amp_id
        self.program = program[:]
        self.ip = 0
        self.input_buffer = input_buffer
        self.output_buffer = output_buffer
        self.paused = False

    def interpret_opcode(self, opcode):
        instruction = opcode % 100
        parameters = opcode // 100

        parameter_mode = [0, 0, 0]
        for idx in range(3):
            parameter_mode[idx] = (parameters % 10)
            parameters = parameters // 10

        return instruction, parameter_mode

    def execute(self):
        opcode = self.program[self.ip]
        instruction, parameter_mode = self.interpret_opcode(opcode)

        if instruction == 1:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]

            result = first_val + second_val
            self.program[self.program[self.ip+3]] = result
            self.ip += 4
        elif instruction == 2:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]

            result = first_val * second_val
            self.program[self.program[self.ip+3]] = result
            self.ip += 4
        elif instruction == 3:
            input_address = self.program[self.ip+1]
            self.program[input_address] = self.input_buffer.pop(0)
            self.ip += 2
        elif instruction == 4:
            output_address = self.program[self.ip+1]
            self.output_buffer.append(self.program[output_address])
            self.ip += 2
            self.paused = True
        elif instruction == 5:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]

            if first_val != 0:
                self.ip = second_val
            else:
                self.ip += 3
        elif instruction == 6:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]

            if first_val == 0:
                self.ip = second_val
            else:
                self.ip += 3
        elif instruction == 7:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]

            if first_val < second_val:
                self.program[self.program[self.ip+3]] = 1
            else:
                self.program[self.program[self.ip+3]] = 0
            self.ip += 4
        elif instruction == 8:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]

            if first_val == second_val:
                self.program[self.program[self.ip+3]] = 1
            else:
                self.program[self.program[self.ip+3]] = 0
            self.ip += 4
        elif instruction == 99:
            global finished
            finished = True


program = list(map(int, open('7.txt').read().split(',')))
max_value = 0
for phase_settings in permutations([5, 6, 7, 8, 9]):
    finished = False
    EA = [phase_settings[0], 0]
    AB = [phase_settings[1]]
    BC = [phase_settings[2]]
    CD = [phase_settings[3]]
    DE = [phase_settings[4]]
    program1 = Program("A", program, EA, AB)
    program2 = Program("B", program, AB, BC)
    program3 = Program("C", program, BC, CD)
    program4 = Program("D", program, CD, DE)
    program5 = Program("E", program, DE, EA)

    programs = [program1, program2, program3, program4, program5]
    current_program_idx = 0
    while not finished:
        current_program = programs[current_program_idx]
        if not current_program.paused:
            current_program.execute()
        else:
            current_program.paused = False
            current_program_idx = (current_program_idx + 1) % 5

    max_value = max(max_value, EA[0])

print(max_value)
