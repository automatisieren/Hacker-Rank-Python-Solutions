if __name__ == "__main__":
    no_students, no_subjects = list(map(int, input().split()))
    note_list = []
    for i in range(no_subjects):
        notes = list(map(float, input().split()))
        note_list.append(notes)
    
    student_tuple = zip(*note_list)
    
    for i in student_tuple:
        print(sum(i)/len(i))