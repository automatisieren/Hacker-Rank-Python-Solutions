from itertools import combinations

if __name__ == "__main__":
    _ = input()
    inp = input().split()
    repeat = int(input().strip())
    comb = list(combinations(inp, repeat))
    score = 0
    for i in comb:
        if 'a' in i:
            score += 1
    print(score/len(comb))    