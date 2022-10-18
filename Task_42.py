if __name__ == "__main__":
    m = int(input().strip())
    m_set = set(map(int, input().split()))
    n = int(input().strip())
    n_set = set(map(int, input().split()))
    diff = m_set.symmetric_difference(n_set)
    diff = sorted(diff)
    for i in range(len(diff)):
        print(diff[i])