from random import choice
from error_handler import exit_with_message


def add_instructions(interpreter):
    add_direction_instructions(interpreter)
    add_operations(interpreter)
    add_conditions(interpreter)
    interpreter.instructions.update({
        '\"': lambda: read_string(interpreter),
        ':': lambda: interpreter.stack.append(
            0 if len(interpreter.stack) == 0 else interpreter.stack[-1]
        ),
        '\\': lambda: swap_top_stack_values(interpreter),
        '$': lambda: interpreter.stack.pop(-1),
        '.': lambda: output_as_integer(interpreter),
        ',': lambda: output_as_ascii_char(interpreter),
        '#': lambda: interpreter.skip_next_instruction(),
        '@': lambda: exit(0),
        ' ': lambda: None,
    })
    add_call_instructions(interpreter)
    add_input_instructions(interpreter)
    add_digits(interpreter)


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
        '-': lambda: stack.append(-stack.pop(-1) + stack.pop(-1)),
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
            choose_direction((1, 0), (-1, 0))),
        "|": lambda: pointer.change_direction(
            choose_direction((0, 1), (0, -1))),
    })

    def choose_direction(if_true, if_false):
        return \
            if_true if len(stack) == 0 or stack.pop(-1) == 0 \
            else if_false


def read_string(interpreter):
    pointer = interpreter.pointer
    pointer.move()
    while pointer.is_inside() \
            and interpreter.get_current_instruction() != '\"':
        interpreter.stack.append(ord(interpreter.get_current_instruction()))
        pointer.move()
    if not pointer.is_inside():
        exit_with_message("Pointer is out of bounds", pointer)


def swap_top_stack_values(interpreter):
    stack = interpreter.stack
    a = stack.pop(-1)
    b = stack.pop(-1)
    stack.append(a)
    stack.append(b)


def output_as_integer(interpreter):
    n = interpreter.stack.pop(-1)
    try:
        print(int(n))
    except ValueError:
        exit_with_message(
            "Top stack value expected to be an integer but it was not",
            interpreter.pointer)


def output_as_ascii_char(interpreter):
    s = interpreter.stack.pop(-1)
    print(chr(s), end='')


def add_call_instructions(interpreter):
    stack = interpreter.stack
    interpreter.instructions.update({
        "g": lambda: get_call(),
        "p": lambda: put_call(),
    })

    def get_call():
        y = stack.pop(-1)
        x = stack.pop(-1)
        if 0 <= x <= interpreter.width and 0 <= y <= interpreter.height:
            stack.append(ord(interpreter.get_char_at(x, y)))
        else:
            stack.append(0)

    def put_call():
        if len(stack) < 3:
            exit_with_message(
                "Not enough values for a put call",
                interpreter.pointer)
        y = stack.pop(-1)
        x = stack.pop(-1)
        v = stack.pop(-1)
        if 0 <= x <= interpreter.width and 0 <= y <= interpreter.height:
            interpreter.change_char_at(x, y, chr(v))
        else:
            exit_with_message(
                "Put call coordinates were out of bounds",
                interpreter.pointer)


def add_input_instructions(interpreter):
    stack = interpreter.stack
    interpreter.instructions.update({
        "&": lambda: get_integer(),
        "~": lambda: get_char(),
    })

    def get_integer():
        n = input()
        try:
            stack.append(int(n))
        except ValueError:
            exit_with_message("Incorrect integer value", interpreter.pointer)

    def get_char():
        c = input()
        if len(c) != 1:
            exit_with_message("Expected a single char", interpreter.pointer)
        stack.append(c)


def add_digits(interpreter):
    interpreter.instructions.update({
        '0': lambda: interpreter.stack.append(0),
        '1': lambda: interpreter.stack.append(1),
        '2': lambda: interpreter.stack.append(2),
        '3': lambda: interpreter.stack.append(3),
        '4': lambda: interpreter.stack.append(4),
        '5': lambda: interpreter.stack.append(5),
        '6': lambda: interpreter.stack.append(6),
        '7': lambda: interpreter.stack.append(7),
        '8': lambda: interpreter.stack.append(8),
        '9': lambda: interpreter.stack.append(9),
    })
