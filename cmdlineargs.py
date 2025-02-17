import sys


def main(args):
    # C-style "Main/Entrypoint" Function
    if len(args) <= 0:
        print("Hello!")
        return
    print("hello", args[0])
    for arg in args:
        print(arg)
    pass


if __name__ == "__main__":
    main(sys.argv[1:])
    # Also see the "argparse" Python Module
