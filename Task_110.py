from numpy import (
                    min,
                    max
                )

if __name__ == "__main__":
    n, _ = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(max(min(arr, axis = 1)))