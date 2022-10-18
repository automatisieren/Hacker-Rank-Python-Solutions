from numpy import (
                    array,
                    transpose
                )
if __name__ == "__main__":
    arr = [list(map(int, input().split())) for _ in range(int(list(map(int, input().split()[0]))[0]))]
    arr = array(arr)
    print(transpose(arr))
    print(arr.flatten())
    