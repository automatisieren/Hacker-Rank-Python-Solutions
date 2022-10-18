from itertools import combinations_with_replacement
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
    
    combs_list = []
    combs = combinations_with_replacement(
                iterable = string,
                r = r       
    )
    combs_list.append({0 : combs})
    sorted_comb_list = sort_combs(
                                comb_tuple = combs_list[0][0])
    for j in sorted_comb_list:
        print(j)