from pointer import Pointer


class Interpreter:
    def __init__(self, path):
        self.width = 0
        self.height = 0
        self.code = self.read_code_from_file(path)
        self.pointer = Pointer(self.width, self.height)
        self.instructions = dict()

    def run(self):
        while self.pointer.is_inside():
            instruction = self.get_current_instruction()

    def read_code_from_file(self, path):
        with open(path) as file:
            lines = []
            for line in file.readlines():
                lines.append(line)
                self.height += 1
                self.width = max(self.width, len(line))
            result = []
            for line in lines:
                result.append(line + ' ' * (self.width - len(line)))
            return result

    def get_current_instruction(self):
        x, y = self.pointer.get_position()
        return self.code[y][x]

    def add_base_instructions(self):
        self.instructions['>'] = lambda:
