from numpy import (
                    eye,
                    set_printoptions
                )

if __name__ == "__main__":
    set_printoptions(legacy='1.13')
    n,m = list(map(int, input().split()))
    print(eye(n,m, k = 0))