from re import match

def fun(s):
    # return True if s is a valid email, else return False
    return bool(match(r"^[\w\-]+[@]{1}[a-zA-Z0-9]+[.]{1}[a-zA-Z]{1,3}$", s))    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)