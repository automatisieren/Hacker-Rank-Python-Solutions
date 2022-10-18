if __name__ == "__main__":
    e = int(input().strip())
    e_set = set(map(int, input().split()))
    f = int(input().strip())
    f_set = set(map(int, input().split()))
    print(len(e_set & f_set))