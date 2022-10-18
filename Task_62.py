cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    # 0-1-1-2-3-5
    result_list = []
    for i in range(n):
        num = 0
        if i == 0 or i == 1:
            result_list.append(i)
        elif i >= 2:
            num = result_list[i-1] + result_list[i-2]
            result_list.append(num)
    return result_list
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    