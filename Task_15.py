def printList(l : list) -> None:
    print(l)

def insertList(l : list, index : int, num : int)-> None:
    l.insert(index, num)

def removeList(l : list, num : int) -> None:
    l.remove(num)
    
def appendList(l : list, num : int) -> None:
    l.append(num)
    
def sortList(l : list, type : str) -> None:
    if type == "normal":
        l.sort()
    elif type == "reverse":
        l.reverse()
        
def popList(l : list) -> None:
    l.pop()

def detectAndApplyList(command : str, inputList : list) -> None:
    if 'print' in command:
        printList(l = inputList)
    elif 'insert' in command:
        _ , index, num = command.split(sep=" ")
        insertList(l = inputList, index = int(index), num = int(num) )
    elif 'remove' in command:
        _ , num = command.split(sep = " ")
        removeList(l = inputList, num = int(num) )
    elif 'append' in command:
        _ , num = command.split(sep = " ")
        appendList(l = inputList, num = int(num) )
    elif 'sort' in command:
        sortList(l = inputList, type = "normal")
    elif 'reverse' in command:
        sortList(l = inputList, type = "reverse")
    elif 'pop' in command:
        popList(l = inputList)

if __name__ == '__main__':
    dummyList = list()
    N = int(input())
    for _ in range(N):
        command = input()
        detectAndApplyList(command = command, inputList = dummyList)