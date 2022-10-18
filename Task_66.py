def wrapper(f):
    def fun(l):
        # complete the function
        new_list = []
        for i in l:
            prefix = "+91 "
            length = len(i)
            if length == 10:
                prefix += i[0:5]
                prefix += " "
                prefix += i[5:10]
            elif length == 11:
                prefix += i[1:6]
                prefix += " "
                prefix += i[6:11]
            elif length == 12:
                prefix += i[2:7]
                prefix += " "
                prefix += i[7:12]
            elif length == 13:
                prefix += i[3:8]
                prefix += " "
                prefix += i[8:13]
            new_list.append(prefix)                                
        return f(new_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
