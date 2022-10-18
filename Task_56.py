if __name__ == "__main__":
    set_a = set(map(int, input().split()))
    no = int(input().strip())
    result = []
    for i in range(no):
        set_1 = set(map(int, input().split()))
        result.append(len(set_1.difference(set_a)) == 0 and (len(set_a) > len(set_1)))
    if False in result:
        print(f"{False}")
    else:
        print(f"{True}")