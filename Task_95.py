from re import (
                findall,
                match,
                search
            )

def check(
        inp : str
) -> str:
    invalid = "Invalid"
    valid = "Valid"
    if len(inp) != 16 and len(inp) != 19:
        print(f"Length is: {len(inp)} - type: {type(len(inp))}")
        return invalid
    count = 0
    sep = 0
    for i in inp:
        if i.isdigit():
            count += 1
        elif i == "-":
            sep += 1
    if count != 16 or (count == 16 and sep != 3 and sep != 0):
        print(f"Count: {count} - Sep: {sep}")
        return invalid
    
    repeat = findall(r"([0-9\-])\1{4,}", inp)
    if len(repeat) > 0:
        return invalid
    
    match1 = bool(match(r"^[4-6]{1}([0-9]){3}-([0-9]){4}-([0-9]){4}-([0-9]){4}$", inp))
    match2 = bool(match(r"^[4-6]{1}([0-9]{15})$", inp))
    match3 = not(bool(search(r"([0-9])\1+-([0-9])\1+", inp)))
    if (match1 or match2) and match3:
        return valid
    print(f"Match 1: {match1}")
    print(f"Match 2: {match2}")
    print(f"Match 3: {match3}")
    return invalid    

if __name__ == "__main__":
    inp = []
    for _ in range(int(input())):
        inp.append(input().strip())
    for i in inp:
        print(check( inp = i))