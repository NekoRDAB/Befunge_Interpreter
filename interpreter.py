from pointer import Pointer
from stack import Stack
from funge_space import FungeSpace
from error_handler import exit_with_message
import instructions_93
import instructions_98
import time


class Interpreter:
    def __init__(self):
        self.space = None
        self.pointer = Pointer(self)
        self.instructions = dict()
        self.stack = Stack()
        instructions_93.add_instructions(self)
        self.skip_next = False
        self.timeout = float("inf")

    def run(self):
        start_time = time.time()
        while True:
            self.execute_instruction()
            if time.time() - start_time > self.timeout:
                exit_with_message("Reached timeout. Terminating", self.pointer)

    def create_space(self, path):
        with open(path) as file:
            self.space = FungeSpace(file)

    def set_timeout(self, timeout):
        self.timeout = timeout

    def add_98_instructions(self):
        instructions_98.add_instructions(self)

    def get_current_instruction(self):
        x, y = self.pointer.get_position()
        return self.space[x, y]

    def get_next_instruction(self):
        x, y = self.pointer.get_next_dest()
        return self.space[x, y]

    def get_char_at(self, x, y):
        return self.space[x, y]

    def change_char_at(self, x, y, v):
        self.space[x, y] = v

    def execute_instruction(self):
        self.execute_given_instruction(self.get_current_instruction())
        self.pointer.move()

    def execute_given_instruction(self, instruction):
        if instruction in self.instructions:
            self.instructions[instruction]()
        else:
            exit_with_message(
                f"Syntax error, unknown instruction: {instruction}",
                self.pointer)

    def skip_next_instruction(self):
        self.skip_next = True
