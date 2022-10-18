from sys import exit
from collections import defaultdict

if __name__ == "__main__":
    """
    The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container,
    but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a
    defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
    """
    n, m = list(map(int, input().split(" ")))
    if (n < 1 or n > 10000):
        exit()
    if (m < 1 or m > 100):
        exit()
    
    groupA = defaultdict(list)
    for i in range(n):
        groupA["elements"].append(input().strip())
    
    groupB = defaultdict(list)
    for i in range(m):
        groupB["elements"].append(input().strip())

    for i in range(m):
        found = False
        element = groupB["elements"][i]
        exist = []
        for index, j in enumerate(groupA["elements"]):
            if j == element:
                exist.append(index)
                found = True
        if not found:
            print(f"{-1}")
        else:
            for elem in exist:
                print(f"{elem + 1}", sep='', end= ' ')
            print("", end="\n")