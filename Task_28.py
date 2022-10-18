def merge_the_tools(string, k):
    # your code goes here
    sub_list = [string[i:i+k] for i in range(0, len(string), k)]
    unique_list = ["".join(dict.fromkeys(word)) for word in sub_list]
    for i in unique_list:
        print(f"{i}")
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)