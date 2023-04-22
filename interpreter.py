from pointer import Pointer
from instructions import add_instructions
from error_handler import exit_with_message


class Interpreter:
    def __init__(self, path):
        self.width = 0
        self.height = 0
        self.code = self.read_code_from_file(path)
        self.pointer = Pointer(self.width, self.height)
        self.instructions = dict()
        self.stack = []
        add_instructions(self)
        self.skip_next = False

    def run(self):
        while self.pointer.is_inside():
            self.execute_instruction()

        if not self.pointer.is_inside():
            exit_with_message("Pointer is out of bounds", self.pointer)

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

    def get_char_at(self, x, y):
        return self.code[y][x]

    def change_char_at(self, x, y, v):
        self.code[y][x] = v

    def execute_instruction(self):
        instruction = self.get_current_instruction()
        if self.skip_next:
            self.skip_next = False
        elif instruction in self.instructions:
            self.instructions[instruction]()
            self.pointer.move()
        else:
            exit_with_message(
                f"Syntax error, unknown instruction: {instruction}",
                self.pointer)

    def skip_next_instruction(self):
        self.skip_next = True
