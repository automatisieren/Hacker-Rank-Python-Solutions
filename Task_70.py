from re import (
            finditer,
            IGNORECASE
            )

if __name__ == "__main__":
    result = list(map(lambda x: x.group(), finditer(r'(?<![aeiou])+([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])+', input(), flags = IGNORECASE)))
    if len(result) > 0:
        for i in result:
            print(f"{i}")
    else:
        print(-1)