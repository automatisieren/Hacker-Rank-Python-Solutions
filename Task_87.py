from collections import deque

def vertical_cube(
                d : deque,
                direction : str
) -> bool:
    if len(d) == 1:
        return True
    else:
        result = []
        if direction == "right":
            print("Trying right...")
            max = d.pop()
            print(f"Picked {max} as max...")
            for _ in range(len(d)):
                result.append(max >= d.pop())
            return all(result)
        elif direction == "left":
            print("Trying left...")
            max = d.popleft()
            print(f"Picked {max} as max...")
            for _ in range(len(d)):
                result.append(max >= d.popleft())
            return all(result)                        
        elif direction == "mix":
            print("Trying mix...")
            stage_winner = []
            for i in range(0, len(d), 2):
                if len(d) > 1:
                    rightmost = d.pop()
                    leftmost = d.popleft()
                    if rightmost >= leftmost:
                        max = rightmost 
                    else:
                        max = leftmost
                    print(f"Round #{i} - Picked {max} as max...")
                    stage_winner.append(max)
                else:
                    max = d.pop()
                    stage_winner.append(max)
            print(f"Stage winners: {stage_winner}")
            for i in range(len(stage_winner)):
                if i != (len(stage_winner) - 1):
                    result.append(stage_winner[i] >= stage_winner[i+1])
            return all(result)
                   
def calculate(
            input_list : list
) -> bool:
    d = deque()
    for i in input_list:
        d.append(i)
    # Try always right
    d_right = d.copy()
    right_result = vertical_cube( 
                                d = d_right, 
                                direction = "right")
    print(f"Right Result: {right_result}")
    d_left = d.copy()
    left_result = vertical_cube( 
                                d = d_left, 
                                direction = "left")
    print(f"Left Result: {left_result}")
    d_mix = d.copy()
    mix_result = vertical_cube( 
                                d = d_mix, 
                                direction = "mix")
    print(f"Mix Result: {mix_result}")
    return right_result or left_result or mix_result

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        _ = input()
        inp = list(map(int, input().split()))
        result = calculate(input_list = inp)
        if result:
            print("Yes")
        else:
            print("No")