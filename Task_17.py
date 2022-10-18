def swap_case(s : str) -> str:
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    r = range(1, 1001)
    if len(s) in r:        
        result = swap_case(s)
        print(result)