from re import U
from typing import Union, NoReturn

def divide(
        a : str,
        b : str ) -> Union[None, NoReturn]:
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")         
        
if __name__ == "__main__":
    n = int(input().strip())
    for i in range(n):
        a, b = list(input().split(" "))
        divide(
            a = a,
            b = b
        )