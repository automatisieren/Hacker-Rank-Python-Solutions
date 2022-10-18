from numpy import (
                    array
                )

if __name__ == "__main__":
    arr = array(list(map(int, input().split())))
    arr.shape = (3,3)
    print(arr)
    
    