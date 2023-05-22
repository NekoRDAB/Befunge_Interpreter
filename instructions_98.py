from error_handler import exit_with_message


def add_instructions(interpreter):
    add_digits(interpreter)


def add_digits(interpreter):
    interpreter.instructions.update({
        'a': lambda: interpreter.stack.push(10),
        'b': lambda: interpreter.stack.push(11),
        'c': lambda: interpreter.stack.push(12),
        'd': lambda: interpreter.stack.push(13),
        'e': lambda: interpreter.stack.push(14),
        'f': lambda: interpreter.stack.push(15),
    })
