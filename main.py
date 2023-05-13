import os
import argparse
from interpreter import Interpreter

EXTENSIONS = [".be", ".bf", ".b93", ".b98", ".befunge"]


def main():
    parser = argparse.ArgumentParser(description='Befunge interpreter')
    parser.add_argument(
        "path", type=str,
        help=f"Absolute path to code file with extensions: {EXTENSIONS}")
    parser.add_argument(
        "timeout", type=bool,
        help="True if the program should be terminated if overtime, False instead"
    )
    args = parser.parse_args()
    if not path_correct(args.path):
        return
    interpreter = Interpreter()
    interpreter.read_code_from_file(args.path)
    if args.timeout:
        interpreter.set_timeout()
    interpreter.run()


def path_correct(path):
    if not os.path.isfile(path):
        print(f"Could not find {path}")
    elif os.path.splitext(path)[-1] not in EXTENSIONS:
        print(f"Invalid extension: {os.path.basename(path)}")
    else:
        return True
    return False


if __name__ == "__main__":
    main()
