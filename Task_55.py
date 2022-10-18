if __name__ == "__main__":
    cases = int(input().strip())
    for i in range(cases):
        _ = int(input().strip())
        a_set = set(map(int, input().split()))
        _ = int(input().strip())
        b_set = set(map(int, input().split()))
        print(len(a_set.difference(b_set)) == 0)