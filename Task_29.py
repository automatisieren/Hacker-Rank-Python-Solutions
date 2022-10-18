
if __name__ == "__main__":
    string = input().strip()
    desired = ""
    for i in range(len(string)):
        char = string[i]
        if char.isalnum():
            try:
                # print(f"Checking: {char}")
                char1 = string[i+1]
                if char == char1:
                    desired = char
                    break
            except:
                break
    
    if desired == "":
        print(f"-1")
    else:
        print(f"{desired}")