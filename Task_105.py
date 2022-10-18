from numpy import (
                    zeros,
                    ones,
                    int64
                )

if __name__ == "__main__":
    shape = tuple(list(map(int, input().split())))
    print(zeros(shape, dtype = int64))
    print(ones(shape, dtype = int64))
