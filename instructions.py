from random import choice


def add_instructions(interpreter):
    add_direction_instructions(interpreter)
    add_operations(interpreter)
    add_conditions(interpreter)


def add_direction_instructions(interpreter):
    pointer = interpreter.pointer
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    interpreter.instructions.update({
        '>': lambda: pointer.change_direction(directions[0]),
        'v': lambda: pointer.change_direction(directions[1]),
        '<': lambda: pointer.change_direction(directions[2]),
        '^': lambda: pointer.change_direction(directions[3]),
        '?': lambda: pointer.change_direction(choice(directions))
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
