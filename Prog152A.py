import sys
sys.setrecursionlimit(7000)


def fact_loop(n):
    product = 1
    for num in range(n, 0, -1):
        product *= num
    return product


def fact(n):
    if n <= 1: return 1   # Base/Ending Case
    return n + fact(n-3)  # Recursive Case


def main():
    num = 3
    sums = 3
    while num != 6999:
        num_fact = fact(num)
        print(f"{num}! = {num_fact}")
        sums += num
        num += 3


if __name__ == '__main__':
    main()
