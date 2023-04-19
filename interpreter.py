import sys
import os


def main():
    if not is_path_correct():
        print("ERROR")
        return


def is_path_correct():
    extensions = [".be", ".bf", ".b93", ".b98", ".befunge"]
    if len(sys.argv) != 2:
        print(f"Usage:\n"
              f"\tpython interpreter.py <absolute path to befunge file>\n"
              f"Extensions: {extensions}")
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not find {sys.argv[1]}")
    elif os.path.splitext(sys.argv[1])[1] not in extensions:
        print(f"{sys.argv[1]} does not have a valid extension")
    else:
        print(f"Filename is correct. Interpreting {os.path.basename(sys.argv[1])}...")
        return True
    return False


if __name__ == "__main__":
    main()
