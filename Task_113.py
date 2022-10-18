from numpy import (
                    inner,
                    outer
                )

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(inner(a,b))
    print(outer(a,b))