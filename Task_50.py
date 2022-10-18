def do_task(
            main_set : set,
            second_set : set,
            command : str
        ) -> set:
    if command == "intersection_update":
        main_set &= second_set
    elif command == "update":
        main_set |= second_set
    elif command == "symmetric_difference_update":
        main_set ^= second_set
    elif command == "difference_update":
        main_set -= second_set
        
    return main_set
        
if __name__ == "__main__":
    no = int(input().strip())
    a = set(map(int, input().split()))
    no_of_operations = int(input().strip())
    for i in range(no_of_operations):
        command, size = input().split()
        second_set = set(map(int, input().split()))
            
        a = do_task(
                main_set = a,
                second_set = second_set,
                command = command
        )
    print(sum(a))