from collections import Counter

if __name__ == "__main__":
    k = int(input().strip())
    numbers = list(map(int, input().split()))
    c = Counter(numbers)
    for i in c:
        if c[i] != k:
            print(i)