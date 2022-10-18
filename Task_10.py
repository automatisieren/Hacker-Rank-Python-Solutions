if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max_no = max(arr)
    arr.sort() 
    for i in range(len(arr),0,-1):
        if arr[i-1] != max_no:
            print(f"{arr[i-1]}")
            break