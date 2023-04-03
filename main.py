import mygroup
def filter_students_by_avg_mark(students, avg_mark):
    filtered_students = []
    for student in students:
        marks = student["marks"]
        avg = sum(marks) / len(marks)
        if avg >= avg_mark:
            filtered_students.append(student)
    return filtered_students

def print_students(students):
    for student in students:
        print("ФИО: " + student["name"] + " " + student["surname"])
        print("Экзамены:", str(student["exams"]))
        print("Оценки:", str(student["marks"]))
        print("-------------")


avg_mark = float(input("Введите средний балл для фильтрации: "))
filtered_students = filter_students_by_avg_mark(mygroup.groupmates, avg_mark)
print_students(filtered_students)
