from itertools import (
                    product
                )

if __name__ == "__main__":
    n, mod = list(map(int, input().split()))
    inp = []
    for _ in range(n):
       inp.append(tuple(map(int, input().split()[1:])))
    possibilities = list(product(*inp))
    results = []
    for i in possibilities:
        result = sum(list(map(lambda x: x ** 2, i)))
        results.append( result % mod)
    print(max(*results, -1))