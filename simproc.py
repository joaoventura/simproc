"""
 Implements an interpreter for the simple microprocessor.

"""


def is_mem_ref(param):
    return param[0] == '[' and param[-1] == ']'


def mem_ref(param):
    return int(param[1:-1])


class Simproc:

    def __init__(self):
        self.memory = [0] * 10      # Memory
        self.r0 = 0                 # Register
        self.code = []              # Program
        self.ip = 0                 # Instruction pointer

    def load(self, code):
        """Load a program."""
        code = code.strip()
        code = [line.strip() for line in code.split('\n')]
        code = [line for line in code if not line.startswith(';')]
        self.code = code

    def fetch(self):
        """Fetches the next instruction"""
        line = self.code[self.ip]
        self.ip += 1
        return line

    def decode(self, line):
        """Decodes an instructions."""
        sep = line.find(' ')
        inst = line[0:sep]
        args = line[sep:]
        args = [arg.strip() for arg in args.split(',')]
        return inst, args

    def run(self):
        """Runs the program."""
        while self.ip < len(self.code):
            line = self.fetch()
            inst, args = self.decode(line)
            self.execute(inst, *args)

    def execute(self, inst, *args):
        """Executes an instruction."""
        if inst == 'NOP':
            pass

        elif inst == 'MOV':
            # Move instruction
            dst, src = args
            if is_mem_ref(src):
                src = self.memory[mem_ref(src)]
            if dst == 'r0':
                self.r0 = int(src)
            else:
                self.memory[int(dst)] = int(src)

        elif inst in ['INC', 'DEC']:
            # Increment and decrement
            dst = args[0]
            if dst == 'r0':
                self.r0 += 1 if inst == 'INC' else -1
            else:
                self.memory[int(dst)] += 1 if inst == 'INC' else -1

        elif inst in ['JZ', 'JNZ', 'JMP']:
            # Jumps
            dst = args[0]
            if inst == 'JNZ' and self.r0 != 0:
                self.ip = int(dst)
            elif inst == 'JZ' and self.r0 == 0:
                self.ip = int(dst)
            elif inst == 'JMP':
                self.ip = int(dst)

    def debug(self):
        """Shows the contents of memory."""
        print(self.memory)
        print('r0 = %s, ip = %s' % (self.r0, self.ip))


if __name__ == '__main__':
    mp = Simproc()
    mp.load("""
        MOV 0, 5 
        MOV r0, [0]
    """)
    mp.run()
    mp.debug()
