def main():
    # Write Mode
    with open("cool.txt", 'w') as f:
        f.write('cool\n')
        f.write('beans')

    # Append Mode
    with open('cool.txt', 'a') as f:
        f.write('\nwowsers')

    # Read Mode
    with open('cool.txt' in 'r') as f:
        for line in f:
            print(line, end='')
    pass


if __name__ == "__main__":
    main()
