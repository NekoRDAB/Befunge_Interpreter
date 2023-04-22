from pointer import Pointer
from instructions import add_instructions


class Interpreter:
    def __init__(self, path):
        self.width = 0
        self.height = 0
        self.code = self.read_code_from_file(path)
        self.pointer = Pointer(self.width, self.height)
        self.instructions = dict()
        add_instructions(self)
        self.stack = []

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


"""
    def add_instructions(self):
        self.add_direction_instructions()

    def add_direction_instructions(self):
        self.instructions.update({
            '>': self.pointer.change_direction((1, 0)),
            'v': self.pointer.change_direction((0, 1)),
            '<': self.pointer.change_direction((-1, 0)),
            '^': self.pointer.change_direction((0, -1)),
        })

    def add_operations(self):
        stack = self.stack
        self.instructions.update({
            '+': stack.append(stack.pop(-1) + stack.pop(-1)),
            '-': stack.append(stack.pop(-1) - stack.pop(-1)),
            '*': stack.append(stack.pop(-1) * stack.pop(-1)),
            '%': stack.append(stack.pop(-1) % stack.pop(-1)),
            '/': self.divide_operation,
            '!': stack.append(stack.pop(-1) == 0),
            '`': stack.append(stack.pop(-1) > stack.pop(-1)),
        })

    def divide_operation(self):
        b = self.stack.pop(-1)
        a = self.stack.pop(-1)
        if a == 0:
            self.stack.append(
                int(input("The divider is zero, what result do you want?"))
            )
        else:
            self.stack.append(b // a)
"""
