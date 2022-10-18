if __name__ == '__main__':
    n = int(input())
    if  (n < 1 or n > 150):
        pass
    else:
        for i in range(1,n+1,1):
            print(f"{i}", end="")