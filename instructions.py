from random import choice
from error_handler import exit_with_message


def add_instructions(interpreter):
    add_direction_instructions(interpreter)
    add_operations(interpreter)
    add_conditions(interpreter)
    interpreter.instructions.update({
        '\"': lambda: read_string(interpreter),
        ':': lambda: interpreter.stack.append(interpreter.stack[-1]),
        '\\': lambda: swap_top_stack_values(interpreter),
        '$': lambda: interpreter.stack.pop(-1),
        '.': lambda: output_as_integer(interpreter),
        ',': lambda: output_as_ascii_char(interpreter),
    })


def add_direction_instructions(interpreter):
    pointer = interpreter.pointer
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    interpreter.instructions.update({
        '>': lambda: pointer.change_direction(directions[0]),
        'v': lambda: pointer.change_direction(directions[1]),
        '<': lambda: pointer.change_direction(directions[2]),
        '^': lambda: pointer.change_direction(directions[3]),
        '?': lambda: pointer.change_direction(choice(directions)),
    })


def add_operations(interpreter):
    stack = interpreter.stack
    interpreter.instructions.update({
        '+': lambda: stack.append(stack.pop(-1) + stack.pop(-1)),
        '-': lambda: stack.append(stack.pop(-1) - stack.pop(-1)),
        '*': lambda: stack.append(stack.pop(-1) * stack.pop(-1)),
        '%': lambda: stack.append(stack.pop(-1) % stack.pop(-1)),
        '/': lambda: divide_operation(),
        '!': lambda: stack.append(stack.pop(-1) == 0),
        '`': lambda: stack.append(stack.pop(-1) > stack.pop(-1)),
    })

    def divide_operation():
        b = interpreter.stack.pop(-1)
        a = interpreter.stack.pop(-1)
        if a == 0:
            interpreter.stack.append(
                int(input("The divider is zero, what result do you want?"))
            )
        else:
            interpreter.stack.append(b // a)


def add_conditions(interpreter):
    pointer = interpreter.pointer
    stack = interpreter.stack
    interpreter.instructions.update({
        "_": lambda: pointer.change_direction(
            choose_direction((1, 0), (1, 0))),
        "|": lambda : pointer.change_direction(
            choose_direction((0, 1), (0, -1))),
    })

    def choose_direction(if_true, if_false):
        return if_true if stack.pop(-1) == 0 else if_false


def read_string(interpreter):
    pointer = interpreter.pointer
    string = ""
    pointer.move()
    while pointer.is_inside() \
            and interpreter.get_current_instruction() != '\"':
        string += interpreter.get_current_instruction()
    if not pointer.is_inside():
        exit_with_message("Pointer is out of bounds", pointer)
    interpreter.stack.append(string)
    pointer.move()


def swap_top_stack_values(interpreter):
    stack = interpreter.stack
    a = stack.pop(-1)
    b = stack.pop(-1)
    stack.append(a)
    stack.append(b)


def output_as_integer(interpreter):
    x = interpreter.stack.pop(-1)
    try:
        print(int(x))
    except ValueError:
        exit_with_message(
            "Top stack value expected to be an integer but it was not",
            interpreter.pointer)


def output_as_ascii_char(interpreter):
    s = interpreter.stack.pop(-1)
    if len(s) != 1:
        exit_with_message(
            "Top stack value expected to be an ascii char but it was not",
            interpreter.pointer)
