for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print(*[j for j in range(1, i + 1)].__add__(([z for z in range(i-1, 0, -1) if i != 1 ])), sep="")
    print(int(pow(((10**i) -1) / 9, 2)))