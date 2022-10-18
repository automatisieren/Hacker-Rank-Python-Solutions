from operator import itemgetter

if __name__ == '__main__':
    all = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        all.append([name, score])
    
    all = sorted(all, key=itemgetter(1))
    _, min_grade = all[0]
    for i in range(len(all)):
        a, b = all[i]
        if b != min_grade:
            sec_lowest = b
            break
    newList = list()
    for i in range(len(all)):
        a, b = all[i]
        if b == sec_lowest:
            newList.append(a)
    newList.sort()
    for i in range(len(newList)):
        print(f"{newList[i]}")