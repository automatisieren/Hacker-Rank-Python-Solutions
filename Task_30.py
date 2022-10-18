from itertools import product


if __name__ == "__main__":
    A = input().split()
    B = input().split()
    result = sorted(tuple(product(map(int, A), map(int, B))))
    for i in result:
        print(f"{i}", end=" ")