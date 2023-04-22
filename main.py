import sys
import os
from interpreter import Interpreter


EXTENSIONS = [".be", ".bf", ".b93", ".b98", ".befunge"]


def main():
    if len(sys.argv) != 2:
        print(f"Usage:\n"
              f"\tpython interpreter.py <absolute path to befunge file>\n"
              f"Extensions: {EXTENSIONS}")
        return
    if not path_correct(sys.argv[1]):
        return
    path = sys.argv[1]
    interpreter = Interpreter(path)
    interpreter.run()


def path_correct(path):
    if not os.path.isfile(path):
        print(f"Could not find {path}")
    elif os.path.splitext(path)[-1] not in EXTENSIONS:
        print(f"{path} does not have a valid extension")
    else:
        return True
    return False


if __name__ == "__main__":
    main()
