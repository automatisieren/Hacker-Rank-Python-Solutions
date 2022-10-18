from collections import deque

def perform_op(
            input : deque,
            command : str,
            no : int
) -> deque:
    if command == "append":
        input.append(no)
    elif command == "appendleft":
        input.appendleft(no)
    elif command == "pop":
        input.pop()
    elif command == "popleft":
        input.popleft()
    
    return input

if __name__ == "__main__":
    no = int(input().strip())
    d = deque()
    for i in range(no):
        input_list = input().split()
        if len(input_list) > 1:
            command, number = input_list
            d = perform_op(
                        input = d,
                        command = command,
                        no = int(number) 
            )
        else:
            command = input_list[0]
            d = perform_op(
                        input = d,
                        command = command,
                        no = None 
            )
    for i in range(len(d)):
        print(d.popleft(), end=" ")        
            
        
