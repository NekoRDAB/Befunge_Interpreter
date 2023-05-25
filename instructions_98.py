from error_handler import exit_with_message


def add_instructions(interpreter):
    add_digits(interpreter)
    add_rotation(interpreter)
    interpreter.instructions.update({
        "'": lambda: fetch(interpreter),
        "s": lambda: store(interpreter),
        ";": lambda: jump_over(interpreter),
        "w": lambda: compare(interpreter),
        "z": lambda: None,
        "x": lambda: absolute_delta(interpreter),
        "q": lambda: quit(interpreter.stack.pop()),
        "r": lambda: interpreter.pointer.revert(),
        "n": lambda: interpreter.stack.clear(),
        "j": lambda: jump_forward(interpreter),
        "k": lambda: iterate(interpreter),
    })


def add_digits(interpreter):
    interpreter.instructions.update({
        'a': lambda: interpreter.stack.push(10),
        'b': lambda: interpreter.stack.push(11),
        'c': lambda: interpreter.stack.push(12),
        'd': lambda: interpreter.stack.push(13),
        'e': lambda: interpreter.stack.push(14),
        'f': lambda: interpreter.stack.push(15),
    })


def add_rotation(interpreter):
    interpreter.instructions.update({
        '[': lambda: interpreter.pointer.rotate(direction=-1),
        ']': lambda: interpreter.pointer.rotate(),
    })


def fetch(interpreter):
    interpreter.pointer.move()
    instruction = interpreter.get_current_instruction()
    interpreter.stack.push(instruction)


def jump_over(interpreter):
    interpreter.pointer.move()
    while interpreter.get_current_instruction() != ';':
        interpreter.pointer.move()


def compare(interpreter):
    b = interpreter.stack.pop()
    a = interpreter.stack.pop()
    if a > b:
        interpreter.instructions[']']()
    elif a < b:
        interpreter.instructions['[']()
    else:
        interpreter.instructions['z']()


def absolute_delta(interpreter):
    dy = interpreter.stack.pop()
    dx = interpreter.stack.pop()
    interpreter.pointer.set_delta((dx, dy))


def store(interpreter):
    x, y = interpreter.pointer.get_next_dest()
    c = interpreter.stack.pop()
    interpreter.change_char_at(x, y, c)


def jump_forward(interpreter):
    s = interpreter.stack.pop()
    interpreter.pointer.move(s=s)


def iterate(interpreter):
    k = interpreter.stack.pop()
    instruction = interpreter.get_next_instruction()
    for i in range(k):
        interpreter.instructions[instruction]()
