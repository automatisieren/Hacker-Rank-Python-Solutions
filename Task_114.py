import numpy

if __name__ == "__main__":
    arr = list(map(float, input().split()))
    x = int(input())
    print(numpy.polyval(arr, x))