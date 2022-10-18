from numpy import (
                    array,
                    concatenate
                )

if __name__ == "__main__":
    n, m, p = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    for _ in range(n):
        arr1.append(list(map(int, input().split())))
    for _ in range(m):
        arr2.append(list(map(int, input().split())))
        
    arr1 = array(arr1)
    arr2 = array(arr2)
    
    print(concatenate((arr1, arr2), axis = 0))