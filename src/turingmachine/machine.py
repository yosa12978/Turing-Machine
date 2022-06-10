from .tape import Tape

class Instruction:
    def __init__(self, in_state, in_symbol, out_state, out_symbol, move):
        self.in_state = in_state
        self.out_state = out_state
        self.in_symbol = in_symbol
        self.out_symbol = out_symbol
        self.move = move

class Machine:
    def __init__(self, program, tape_size, states, start, halt):
        self.tape = Tape(tape_size)
        self.tape_size = tape_size
        self.program = program
        self.position = tape_size//2+1
        self.states = states
        self.halt_state = halt
        self.current_state = start

    def run(self):
        while self.current_state != self.halt_state:
            symbol = self.tape.tape[self.position]
            for i in self.program:
                if i.in_state == self.current_state and i.in_symbol == symbol:
                    self.current_state = i.out_state
                    self.tape.tape[self.position] = i.out_symbol
                    if i.move == "R":
                        self.position+=1
                    elif i.move == "L":
                        self.position-=1
                    break
            print(str(self.tape)+f" - {self.current_state} {self.position-self.tape_size//2}")
        return self.tape.tape
