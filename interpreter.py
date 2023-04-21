class Interpreter:
    def __init__(self, path):
        self.code = self.read_code(path)

    def read_code(self, path):
        with open(path) as file:
            return [line for line in file.readlines()]