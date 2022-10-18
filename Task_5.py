from sys import exit
if __name__ == '__main__':
    n = int(input())
    if n > 20 and n < 1:
        exit()
    else:
        for i in range(0, n, 1):
            print(f"{i ** 2}")