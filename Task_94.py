from re import sub


if __name__ == "__main__":
    inp = ""
    repeat = int(input())
    for i in range(repeat):
        inp += input()
        if i != repeat -1:
            inp += "\n"
    inp = sub(r"\s{1}&&(?=[\s]{1})", " and", inp)
    print(sub(r"\s{1}\|\|(?=[\s]{1})", " or", inp))