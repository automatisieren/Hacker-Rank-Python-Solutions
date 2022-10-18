from itertools import combinations

def list_to_str(
            a : tuple
) -> str:
    string = ""
    for i in a:
        string += i
    return string

def sort_combs (
            comb_tuple : tuple,
    ) -> list:
    new_list = []
    for i in comb_tuple:
        new_list.append(list_to_str(
                                a = sorted(i)
        ))
    return sorted(new_list)

if __name__ == "__main__":
    string, r = list(input().split())
    r = int(r)
    for i in range(r):
        combs_list = []
        combs = combinations(
                    iterable = string,
                    r = i + 1        
        )
        combs_list.append({i : combs})
        sorted_comb_list = sort_combs(
                                    comb_tuple = combs_list[0][i])
        for j in sorted_comb_list:
            print(j)