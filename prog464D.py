from random import randint
import numpy as np
# import numpy as np (have to do 'pip install numpy' in the terminal)


def print_matrix(mat):
    for row in mat:
        for num in row:
            print(f"{num:3d} ", end="")
        print()


def transpose():
    pass


def main():
    mat1 = []
    mat2 = []
    for r in range(5):
        row1 = []
        for c in range(5):
            row1.append(randint(-50, 99))
        mat1.append(row1)
        mat2.append(row1)

    print("Matrix 1:")
    print_matrix(mat1)

    print("\nTransposed:")
    print_matrix(mat1.transpose())


if __name__ == "__main__":
    main()
