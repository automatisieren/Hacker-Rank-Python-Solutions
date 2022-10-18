from re import findall

if __name__ == "__main__":
    inp = input().strip()
    lower = sorted(findall("[a-z]", inp))
    upper = sorted(findall("[A-Z]", inp))
    odd = sorted(findall("[13579]", inp))
    even = sorted(findall("[02468]", inp))
    print("".join(list(map(lambda x: str(x), lower + upper + odd + even))))