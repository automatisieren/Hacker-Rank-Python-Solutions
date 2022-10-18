from re import match

def check_if_valid_mail(
                        string : str
)-> bool:
    return bool(match('^[a-zA-Z]{1}\w+[.-]*\w*[.-]*[@]{1}[a-zA-Z]+[.]{1}[a-zA-Z]{1,3}$', string))

if __name__ == "__main__":
    repeat = input().strip()
    for _ in range(int(repeat)):
        name, email = input().split()
        email = email.removeprefix('<').removesuffix('>')
        res = check_if_valid_mail(string = email)
        if res:
            print("Detected" + name + " <" + email + ">")
        
        