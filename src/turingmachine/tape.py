class Tape:
    def __init__(self, size):
        self.tape = [0 for i in range(size)]
        self.size = size
    def __str__(self):
        return str(self.tape).replace("[", "").replace("]", "").replace(",", "")