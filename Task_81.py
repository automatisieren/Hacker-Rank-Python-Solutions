if __name__ == "__main__":
    _, n = list(map(int, input().split()))
    input_list = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    score = 0
    for i in input_list:
        if i in A:
            score += 1
        if i in B:
            score -= 1
    print(f"{score}")