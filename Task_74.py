# Enter your code here. Read input from STDIN. Print output to STDOUT
from re import match

def check_if_phone(
                    string : str
                ) -> str:
    res = bool(match('^[7-9]\d{9}$', string))
    if res:
        return "YES"
    return "NO"

if __name__ == "__main__":
    repeat = input().strip()
    result = [check_if_phone(string = input()) for _ in range(int(repeat))]
    print("\n".join(str(x) for x in result))   