import sys


def exit_with_message(message, pointer):
    print(f"Error occurred while interpreting {sys.argv[1]} at location {pointer.get_position()}")
    print(f"The program stopped with message:")
    print(f"\t{message}")
    sys.exit(0)