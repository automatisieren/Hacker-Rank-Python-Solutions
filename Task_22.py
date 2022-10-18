def isAlphaNum(s : str) -> None:
    flag = False
    for i in range(len(s)):
        flag = s[i].isalnum()
        if flag == True:
            break
    print(f"{flag}")

def isAlpha(s : str) -> None:
    flag = False
    for i in range(len(s)):
        flag = s[i].isalpha()
        if flag == True:
            break
    print(f"{flag}")

def isDigit(s : str) -> None:
    flag = False
    for i in range(len(s)):
        flag = s[i].isdigit()
        if flag == True:
            break
    print(f"{flag}")
    
def isLower(s : str) -> None:
    flag = False
    for i in range(len(s)):
        flag = s[i].islower()
        if flag == True:
            break
    print(f"{flag}")
    
def isUpper(s : str) -> None:
    flag = False
    for i in range(len(s)):
        flag = s[i].isupper()
        if flag == True:
            break
    print(f"{flag}")

def checkStr(string : str) -> None:
    isAlphaNum( s = string )
    isAlpha(s = string)
    isDigit(s = string)
    isLower(s = string)
    isUpper(s = string)

if __name__ == '__main__':
    s = input()
    checkStr(string = s)