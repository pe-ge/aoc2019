class Intcode:
    def __init__(self, program, input_buffer, output_buffer):
        self.program = program
        self.input_buffer = input_buffer
        self.output_buffer = output_buffer
        self.ip = 0
        self.rb = 0
        self.running = True

    def interpret_opcode(self, opcode):
        instruction = opcode % 100
        parameters = opcode // 100

        parameter_mode = [0, 0, 0]
        for idx in range(3):
            parameter_mode[idx] = (parameters % 10)
            parameters = parameters // 10

        return instruction, parameter_mode

    def execute(self):
        if not self.running:
            return True

        opcode = self.program[self.ip]
        if opcode == 99:
            self.running = False
            return
        instruction, parameter_mode = self.interpret_opcode(opcode)

        if instruction == 1:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]
            elif parameter_mode[0] == 2:
                first_val = self.program[first_val + self.rb]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]
            elif parameter_mode[1] == 2:
                second_val = self.program[second_val + self.rb]

            result = first_val + second_val
            output_address = self.program[self.ip+3]
            if parameter_mode[2] == 2:
                output_address += self.rb

            self.program[output_address] = result
            self.ip += 4
        elif instruction == 2:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]
            elif parameter_mode[0] == 2:
                first_val = self.program[first_val + self.rb]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]
            elif parameter_mode[1] == 2:
                second_val = self.program[second_val + self.rb]

            result = first_val * second_val
            output_address = self.program[self.ip+3]
            if parameter_mode[2] == 2:
                output_address += self.rb

            self.program[output_address] = result
            self.ip += 4
        elif instruction == 3:
            input_address = self.program[self.ip+1]
            if parameter_mode[0] == 2:
                input_address += self.rb
            input_val = self.input_buffer.pop(0)
            self.program[input_address] = ord(input_val)
            self.ip += 2
        elif instruction == 4:
            output_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                output_val = self.program[output_val]
            elif parameter_mode[0] == 2:
                output_val = self.program[output_val + self.rb]
            self.output_buffer.append(output_val)
            self.ip += 2
        elif instruction == 5:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]
            elif parameter_mode[0] == 2:
                first_val = self.program[first_val + self.rb]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]
            elif parameter_mode[1] == 2:
                second_val = self.program[second_val + self.rb]

            if first_val != 0:
                self.ip = second_val
            else:
                self.ip += 3
        elif instruction == 6:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]
            elif parameter_mode[0] == 2:
                first_val = self.program[first_val + self.rb]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]
            elif parameter_mode[1] == 2:
                second_val = self.program[second_val + self.rb]

            if first_val == 0:
                self.ip = second_val
            else:
                self.ip += 3
        elif instruction == 7:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]
            elif parameter_mode[0] == 2:
                first_val = self.program[first_val + self.rb]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]
            elif parameter_mode[1] == 2:
                second_val = self.program[second_val + self.rb]

            output_address = self.program[self.ip+3]
            if parameter_mode[2] == 2:
                output_address += self.rb

            if first_val < second_val:
                self.program[output_address] = 1
            else:
                self.program[output_address] = 0
            self.ip += 4
        elif instruction == 8:
            first_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                first_val = self.program[first_val]
            elif parameter_mode[0] == 2:
                first_val = self.program[first_val + self.rb]

            second_val = self.program[self.ip+2]
            if parameter_mode[1] == 0:
                second_val = self.program[second_val]
            elif parameter_mode[1] == 2:
                second_val = self.program[second_val + self.rb]

            output_address = self.program[self.ip+3]
            if parameter_mode[2] == 2:
                output_address += self.rb

            if first_val == second_val:
                self.program[output_address] = 1
            else:
                self.program[output_address] = 0
            self.ip += 4
        elif instruction == 9:
            val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                val = self.program[val]
            elif parameter_mode[0] == 2:
                val = self.program[val + self.rb]
            self.rb += val
            self.ip += 2


program = list(map(int, open('21.txt').read().split(',')))
program.extend([0] * 10000)

rule_1 = ['NOT A J']                                             # .xxxxxxxx
rule_2 = ['NOT C T', 'AND A T', 'AND D T', 'AND H T', 'OR T J']  # #x.#xxx#x
rule_3 = ['NOT B T', 'AND A T', 'AND C T', 'AND D T', 'OR T J']  # #.##xxxxx

rules = [rule_1, rule_2, rule_3]
input_buffer = []
for rule in rules:
    input_buffer.extend(list('\n'.join(rule) + '\n'))
input_buffer.extend(list('RUN\n'))

output_buffer = []
intcode = Intcode(program, input_buffer, output_buffer)
while True:
    if intcode.execute():
        break
    if intcode.output_buffer:
        try:
            char = intcode.output_buffer.pop(0)
            print(chr(char), end='')
        except ValueError:
            print(char)
