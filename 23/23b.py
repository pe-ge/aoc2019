class NAT:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Intcode:
    def __init__(self, program, input_buffer, output_buffer, nat):
        self.program = program
        self.input_buffer = input_buffer
        self.output_buffer = output_buffer
        self.ip = 0
        self.rb = 0
        self.running = True
        self.idling = False
        self.nat = nat

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
            print('Finished')
            return

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
            input_val = self.input_buffer.pop(0) if self.input_buffer else -1

            # idling
            self.idling = True if input_val == -1 else False
            self.program[input_address] = input_val
            self.ip += 2
        elif instruction == 4:
            self.idling = False
            output_val = self.program[self.ip+1]
            if parameter_mode[0] == 0:
                output_val = self.program[output_val]
            elif parameter_mode[0] == 2:
                output_val = self.program[output_val + self.rb]
            self.output_buffer.append(output_val)
            if len(self.output_buffer) == 3:
                address, x, y = self.output_buffer
                if address == 255:
                    nat.x = x
                    nat.y = y
                else:
                    inputs[address].append(x)
                    inputs[address].append(y)
                self.output_buffer = []
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


program = list(map(int, open('23.txt').read().split(',')))
program.extend([0] * 100000)

N = 50
inputs = [[i] for i in range(N)]
outputs = [[] for _ in range(N)]
nat = NAT(None, None)
intcodes = [Intcode(program[:], inputs[i], outputs[i], nat) for i in range(N)]

delivered = set()

while True:
    all_idling = True
    for i in range(N):
        intcodes[i].execute()
        all_idling = all_idling and intcodes[i].idling

    if all_idling and nat.x is not None:
        intcodes[0].input_buffer.append(nat.x)
        intcodes[0].input_buffer.append(nat.y)

        if nat.y in delivered:
            print(nat.y)

        delivered.add(nat.y)

        nat.x = None
        nat.y = None
