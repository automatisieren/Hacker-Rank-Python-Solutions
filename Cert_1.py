def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    new_str = ""
    index_list = []
    for i in range(len(sentence)):
        if sentence[i].islower():
            new_str += sentence[i].upper()
        elif sentence[i].isupper():
            new_str += sentence[i].lower()
        else:
            new_str += sentence[i]
            index_list.append(i)
    newest = ""
    print(index_list)
    index_list = sorted(index_list, reverse = True)
    print(index_list) 
    print(f"New str: {new_str}")
    print(new_str[11:])
    print(new_str[8:11])
    print(new_str[:8]) 
    for i in range(0, len(index_list) + 1, 1):
        print(f"i is {i}")
        if i == 0:
            newest += new_str[index_list[i]+1:]
            newest += " "
            print(f"Newest: {newest}")
        elif i == len(index_list):
            newest += new_str[:index_list[i-1]]
            print(f"Newest: {newest}")
        else:
            newest += new_str[index_list[i]+1:index_list[i-1]]
            newest += " "                        
            print(f"Newest: {newest}")
    return newest
            
if __name__ == '__main__':

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
