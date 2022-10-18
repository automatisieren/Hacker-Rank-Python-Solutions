from numpy import (
                    add,
                    subtract,
                    multiply,
                    floor_divide,
                    mod,
                    power
                )

if __name__  == "__main__":
    n, _ = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    for _ in range(n):
        arr1.append(list(map(int, input().split())))
    for _ in range(n):
        arr2.append(list(map(int, input().split())))
    operations = [add, subtract, multiply, floor_divide, mod, power]
    [print(func(arr1, arr2)) for func in operations] 