def count_substring(string : str, sub_string : str) -> int:
    interval = len(sub_string)
    counter = 0
    for i in range(0, len(string)):
        if string[i:i+interval] == sub_string:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)