if __name__ == "__main__":
    a = int(input())
    b = int(input())
    res = int(a/b)
    print(f"{res}\n{a%b}\n{divmod(a,b)}")