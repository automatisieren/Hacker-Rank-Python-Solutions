
if __name__ == "__main__":
    e = int(input().strip())
    eng_set = set(map(int, input().split()))
    f = int(input().strip())
    fr_set = set(map(int, input().split()))
    print(len(eng_set | fr_set))    