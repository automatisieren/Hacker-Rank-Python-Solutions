from itertools import groupby

if __name__ == "__main__":
    inp = input().strip()
    groups = [list(g) for _, g in groupby(inp)]
    for i in groups:
        print((len(i), int(i[0])), end=" ")   