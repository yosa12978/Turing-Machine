from turingmachine import machine

if __name__ == "__main__":
    # Here loaded test program "busy beaver" for 2 states
    i1 = machine.Instruction("q0", 0, "q1", 1, "R")
    i2 = machine.Instruction("q0", 1, "q1", 1, "L")
    i3 = machine.Instruction("q1", 0, "q0", 1, "L")
    i4 = machine.Instruction("q1", 1, "halt", 1, "R")
    program = [i1, i2, i3, i4]
    states = ["q0", "q1", "halt"]
    halt = "halt"
    start = "q0"
    tape_size = 11

    m = machine.Machine(program, tape_size, states, start, halt)
    m.run()
    """
    returns:
    0 0 0 0 0 0 1 0 0 0 0 - q1 2
    0 0 0 0 0 0 1 1 0 0 0 - q0 1
    0 0 0 0 0 0 1 1 0 0 0 - q1 0
    0 0 0 0 0 1 1 1 0 0 0 - q0 -1
    0 0 0 0 1 1 1 1 0 0 0 - q1 0
    0 0 0 0 1 1 1 1 0 0 0 - halt 1
    """