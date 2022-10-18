from numpy import (
                    mean,
                    var,
                    std,
                    printoptions
                )

if __name__ == "__main__":
    printoptions(legacy="1.13")
    n, _ = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(mean(arr, axis = 1))
    print(var(arr, axis = 0))
    print(round(std(arr), 11))