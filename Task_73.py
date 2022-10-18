from re import search

def check_regex(
                regex : str
) -> bool:
    # [].+*\b\B\A\Z\w\W\d\D\s\S
    try:
        repetition = not(bool(search('.*([+*?](?=[+*?])).*', regex))) # Should be true search('.*([+*?]{0}|[+*?]{1}(?![+*?])).*', b)
        beginning = not(bool(search(r'^\\Z', regex))) # Should be false
        ending = not(bool(search(r'\\A$', regex))) # Should be false
        notation = not(bool(search('^/|/$', regex))) # Should be true
        #print(f"Rep: {repetition} - Beg: {beginning} End: {ending}")
        return (repetition and beginning) and ending and notation
    except:
        return False
if __name__ == "__main__":
    repeat = input().strip()
    result = [check_regex(regex = input()) for _ in range(int(repeat))]
    for i in result:
        print(i)    