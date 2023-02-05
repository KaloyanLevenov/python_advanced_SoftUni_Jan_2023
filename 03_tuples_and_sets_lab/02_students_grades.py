def add_students(number):
    register = {}
    for student in range(number_of_students):
        name, grade = input().split()
        if name not in register.keys():
            register[name] = []
        register[name].append(float(grade))
    return register


def print_func(register):
    for student, grades in register.items():
        average_grade = sum(grades) / len(grades)
        unpacked_grades = " ".join(map(lambda grade: f'{grade:.2f}', grades))
        print(f"{student} -> {unpacked_grades} (avg: {average_grade:.2f})")


number_of_students = int(input())
student_register = add_students(number_of_students)
print_func(student_register)
