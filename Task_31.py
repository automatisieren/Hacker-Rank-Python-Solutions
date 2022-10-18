from itertools import permutations

if __name__ == "__main__":
    string, length = input().split()
    length = int(length)
    result = sorted(list(permutations(list(string), length)))
    for i in result:
        print(f"{''.join(i)}")