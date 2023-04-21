import sys
import os
from interpreter import Interpreter


def main():
    if not arguments_correct():
        return
    path = sys.argv[1]
    interpreter = Interpreter(path)
    interpreter.run()


def arguments_correct():
    extensions = [".be", ".bf", ".b93", ".b98", ".befunge"]
    if len(sys.argv) != 2:
        print(f"Usage:\n"
              f"\tpython interpreter.py <absolute path to befunge file>\n"
              f"Extensions: {extensions}")
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not find {sys.argv[1]}")
    elif os.path.splitext(sys.argv[1])[-1] not in extensions:
        print(f"{sys.argv[1]} does not have a valid extension")
    else:
        return True
    return False


if __name__ == "__main__":
    main()
