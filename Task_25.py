def form_line( size : int,  step_no : int ) -> str:
    # step_no should start from 0
    text = ""
    starter = 96
    if step_no == 0 or step_no == ((size * 2) - 2) :
        text += chr(starter + size)
    else:
        for i in range(0, step_no, 1):
            text += chr(starter + (size - i))
            text += "-"
        text += chr(starter + (size - step_no)) + "-"
        for i in range(step_no, 0, -1):
            text += chr(starter + (size - i + 1))
            if size != (size - i + 1):
                text += "-"
    return text

def print_rangoli(size : int) -> None:
    # your code goes here
    for i in range(0, size, 1):
        print("-" * ( (abs( i - size) * 2) - 2 ), end="")
        print(form_line(size = size, step_no = i), end="")
        print("-" * ( (abs( i - size) * 2) - 2 ))

    for i in range(size - 2, -1, -1):
        print("-" * ( (abs( i - size) * 2) - 2 ), end="")
        print(form_line(size = size, step_no = i), end="")
        print("-" * ( (abs( i - size) * 2) - 2 ))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)