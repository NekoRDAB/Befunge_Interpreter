import os
import argparse
from interpreter import Interpreter
from multiprocessing import Process

EXTENSIONS = [".be", ".bf", ".b93", ".b98", ".befunge"]
TIMEOUT = 60


def main():
    parser = argparse.ArgumentParser(description='Befunge interpreter')
    parser.add_argument(
        "path", type=str,
        help=f"Absolute path to code file with extensions: {EXTENSIONS}")
    args = parser.parse_args()
    if not path_correct(args.path):
        return
    interpreter = Interpreter()
    interpreter.read_code_from_file(args.path)
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
    process = Process(target=main)
    process.start()
    process.join(TIMEOUT)
    if process.is_alive():
        print("Reached timeout. Terminating")
        process.kill()
