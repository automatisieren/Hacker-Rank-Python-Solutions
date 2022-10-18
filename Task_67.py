import operator

def person_lister(f):
    def inner(people):
        # complete the function
        x = operator.itemgetter(2)
        for i in people:
            i[2] = int(i[2])
        new_list = sorted(people, key=x)
        for i in new_list:
            i[2] = str(i[2])
        new_list2 = [f(i) for i in new_list]
        return new_list2
                    
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')