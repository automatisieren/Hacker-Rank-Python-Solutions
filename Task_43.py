from sys import exit

if __name__ == "__main__":
    no = int(input().strip())
    if no < 1 or no > 1000:
        exit()
    unique_set = {}
    unique_list = []
    for _ in range(no):
        unique_list.append(input().strip())
    print(len(set(unique_list)))