class TuringMachine:
    def __init__(self, tape, program, alphabet):
        self.tape = list(tape)
        self.head = 0
        self.state = 'q0'
        self.program = self.load_program(program)
        self.alphabet = self.load_alphabet(alphabet)
        self.output = []

    def load_program(self, program_file):
        program = {}
        with open(program_file, 'r') as f:
            for line in f:
                parts = line.strip().split('->')
                condition = parts[0].strip().split(',')
                action = parts[1].strip().split(',')
                program[(condition[0].strip(), condition[1].strip())] = (action[0].strip(), action[1].strip(), action[2].strip())
        return program

    def load_alphabet(self, alphabet_file):
        with open(alphabet_file, 'r') as f:
            return set(line.strip() for line in f)

    def step(self):
        current_symbol = self.tape[self.head] if self.head < len(self.tape) else '_'
        if (self.state, current_symbol) in self.program:
            self.output.append((self.tape.copy(), self.head, self.state))
            action = self.program[(self.state, current_symbol)]
            self.state = action[0]
            self.tape[self.head] = action[1]
            self.head += 1 if action[2] == 'R' else -1
            if self.head < 0:
                self.tape.insert(0, '_')
                self.head = 0
            elif self.head >= len(self.tape):
                self.tape.append('_')
        else:
            raise Exception("No transition defined for state: {} and symbol: {}".format(self.state, current_symbol))

    def run(self):
        while self.state != 'qf':
            self.step()

    def save_output(self, output_file):
        with open(output_file, 'w') as f:
            for tape_state, head_position, command in self.output:
                f.write(''.join(tape_state) + '\n')
                f.write('^' + '\n')
                f.write(f"{command}\n")

if __name__ == "__main__":
    tm = TuringMachine(tape='11*111', program='prog.txt', alphabet='alphabet.txt')
    tm.run()
    tm.save_output('output.txt')
