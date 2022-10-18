"""
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
If a new entry overwrites an existing entry, the original insertion position is left unchanged.
"""
from collections import OrderedDict
from sys import exit

if __name__ == "__main__":
    no = int(input().strip())
    if no < 0 or no > 100:
        exit()
    itemDict = OrderedDict()
    for _ in range(no):
        items = list(input().split())
        item_name = ""
        for i in range(len(items)):
            if i == len(items) - 1:
                item = int(items[i])
            else:
                item_name = item_name +  " " + items[i]
        item_name = item_name.strip()
        if item_name in itemDict:
            ex = itemDict[item_name]
            item += ex
        itemDict[item_name] = item
    for key, value in itemDict.items():
        print(f"{key} {value}")
        
    