def add_instructions(interpreter):
    add_direction_instructions(interpreter)


def add_direction_instructions(interpreter):
    pointer = interpreter.pointer
    interpreter.instructions.update({
        '>': lambda: pointer.change_direction((1, 0)),
        'v': lambda: pointer.change_direction((0, 1)),
        '<': lambda: pointer.change_direction((-1, 0)),
        '^': lambda: pointer.change_direction((0, -1)),
    })


def add_operations(interpreter):
    stack = interpreter.stack
    interpreter.instructions.update({
        '+': lambda: stack.append(stack.pop(-1) + stack.pop(-1)),
        '-': lambda: stack.append(stack.pop(-1) - stack.pop(-1)),
        '*': lambda: stack.append(stack.pop(-1) * stack.pop(-1)),
        '%': lambda: stack.append(stack.pop(-1) % stack.pop(-1)),
        '/': lambda: divide_operation(interpreter),
        '!': lambda: stack.append(stack.pop(-1) == 0),
        '`': lambda: stack.append(stack.pop(-1) > stack.pop(-1)),
    })


def divide_operation(interpreter):
    b = interpreter.stack.pop(-1)
    a = interpreter.stack.pop(-1)
    if a == 0:
        interpreter.stack.append(
            int(input("The divider is zero, what result do you want?"))
        )
    else:
        interpreter.stack.append(b // a)