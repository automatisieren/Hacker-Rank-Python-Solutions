from numpy import (
                    floor,
                    ceil,
                    rint,
                    set_printoptions
                )

if __name__ == "__main__":
    set_printoptions(legacy = "1.13")
    arr = list(map(float, input().split()))
    operations = [floor, ceil, rint]
    [print(func(arr)) for func in operations]