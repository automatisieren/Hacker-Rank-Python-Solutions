def calculate(word : str) -> list:
    kevin = 0
    stuart = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(word)):
        if word[i] in vowels:
            kevin += len(word) - i
        else:
            stuart += len(word) - i
    return [kevin, stuart]        
    
def minion_game(string : str) -> None:
    # your code goes here

    kevin_score, stuart_score = calculate(word = string)
    
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print(f"Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)