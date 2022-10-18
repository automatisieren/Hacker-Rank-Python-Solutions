from numpy import dot

if __name__ == "__main__":
    arr1 = []
    arr2 = []
    n = int(input())
    for _ in range(n):
        arr1.append(list(map(int, input().split())))
    for _ in range(n):
        arr2.append(list(map(int, input().split())))
    print(dot(arr1, arr2))