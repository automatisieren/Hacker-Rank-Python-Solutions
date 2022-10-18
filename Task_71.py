from re import finditer

if __name__ == "__main__":
    inp = input().strip()
    desired = input().strip()
    result = list(map(lambda x: (x.start(), x.end() + len(desired) - 1), finditer(r"(?=("+ desired + "))", inp)))
    if len(result) > 0:
        print("\n".join(str(x) for x in result))
    else:
        print(str((-1, -1)))