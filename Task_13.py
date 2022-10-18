from sys import exit

def printPipe(pipe : int)-> str:
    output = ""
    for a in range(pipe):
        output += ".|."
    return output

if __name__ == "__main__":
    line = input().split()
    line = list(map(int, line))
    rows, cols = line
    if rows < 5 or rows > 100:
        exit()
    if cols != rows * 3:
        exit()
    mat = "WELCOME"
    for i in range(int(rows / 2)):
        pipe = (i * 2) + 1
        print("-" * int(((cols - (pipe * 3)) / 2)), end="")
        print(printPipe(pipe = pipe), end="")
        print("-" * int(((cols - (pipe * 3)) / 2)), end="")
        print("\n")
    print("-" * int(((cols - 7) / 2)) + mat + "-" * int(((cols - 7) / 2)) + "\n", end="")
    for i in reversed(range(int(rows / 2))):
        pipe = (i * 2) + 1
        print("-" * int(((cols - (pipe * 3)) / 2)), end="")
        print(printPipe(pipe = pipe), end="")
        print("-" * int(((cols - (pipe * 3)) / 2)), end="")
        print("\n", end="")
