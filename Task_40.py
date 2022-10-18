from collections import namedtuple

if __name__ == "__main__":
    no = int(input().strip())
    cols = list(input().split())
    student_tuple = namedtuple('Student', cols)
    total = 0
    for _ in range(no):
        values = list(input().split())
        student = student_tuple(*values)
        total +=  int(student.MARKS)
    print(total / no)