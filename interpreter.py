from pointer import Pointer
from stack import Stack
from instructions import add_instructions
from error_handler import exit_with_message
import time


class Interpreter:
    def __init__(self):
        self.width = 80
        self.height = 25
        self.code = None
        self.pointer = Pointer(self.width, self.height)
        self.instructions = dict()
        self.stack = Stack()
        add_instructions(self)
        self.skip_next = False
        self.timeout = float("inf")

    def run(self):
        start_time = time.time()
        while self.pointer.is_inside():
            self.execute_instruction()
            if time.time() - start_time > self.timeout:
                exit_with_message("Reached timeout. Terminating", self.pointer)

        if not self.pointer.is_inside():
            exit_with_message("Pointer is out of bounds", self.pointer)

    def read_code_from_file(self, path):
        with open(path) as file:
            result = []
            for line in file.readlines():
                current_line = line.replace('\n', '')
                result.append(current_line + ' ' * (self.width - len(current_line)))
            self.code = result + [" " * 80] * (25 - len(result))

    def set_timeout(self, timeout):
        self.timeout = timeout

    def get_current_instruction(self):
        x, y = self.pointer.get_position()
        return self.code[y][x]

    def get_char_at(self, x, y):
        return self.code[y][x]

    def change_char_at(self, x, y, v):
        self.code[y] = self.code[y][:x] + v + self.code[y][x+1:]

    def execute_instruction(self):
        self.execute_given_instruction(self.get_current_instruction())
        self.pointer.move()

    def execute_given_instruction(self, instruction):
        if self.skip_next:
            self.skip_next = False
        elif instruction in self.instructions:
            self.instructions[instruction]()
        else:
            exit_with_message(
                f"Syntax error, unknown instruction: {instruction}",
                self.pointer)

    def skip_next_instruction(self):
        self.skip_next = True
