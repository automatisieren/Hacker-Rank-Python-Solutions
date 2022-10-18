from numpy import linalg

if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        arr.append(list(map(float, input().split())))
    print(round(linalg.det(arr), 2))