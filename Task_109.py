from numpy import (
                    sum,
                    prod
                )

if __name__ == "__main__":
    n, _ = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(prod(sum(arr, axis = 0), axis = 0))