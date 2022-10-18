from sys import exit

def calcAvg(student_dict : dict, name : str)-> float:
    total = 0
    marks = student_dict[name]
    for a in range(len(marks)):             
        total += float(marks[a])
    return total / len(marks) 

if __name__ == '__main__':
    n = int(input())
    if n < 2 or n > 10:
        exit()
    mark_counter = 0
    student_marks = {}
    for _ in range(n):
        if mark_counter > 100:
            exit()
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        mark_counter += 1
    query_name = input()
    print(format(calcAvg(student_dict=student_marks, name=query_name), '.2f'))
