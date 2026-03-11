# /usr/bin/python3
from sys import argv


def main(argv: list[str]) -> None:
    """Take arguments from the terminal and check them"""
    print("=== Command Quest ===")

    list_args: list[str] = argv
    if len(list_args) == 1:
        print("No arguments provided!")
        print(f"Program name: {list_args[0]}!")
        print(f"Total arguments: {len(list_args)}!")
    else:
        print(f"Arguments received: {len(list_args)}")
        i: int = 0
        for arg in list_args:
            if i == 0:
                print(f"Program name: {arg}")
            else:
                print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {len(list_args)}")


if __name__ == "__main__":
    main(argv)
