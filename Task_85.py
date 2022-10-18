from collections import Counter

if __name__ == "__main__":
    inp = [input().strip() for _ in range(int(input()))]
    counter = Counter(inp)
    print(len(counter))
    for k,v in counter.items():
        print(v, end=" ")
        