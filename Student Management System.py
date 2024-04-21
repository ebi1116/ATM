class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, grade):
        student = Student(student_id, name, age, grade)
        self.students.append(student)
        print(f"Student {name} added successfully.")

    def display_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"Student found - ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
                return
        print("Student not found.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student.name} removed successfully.")
                return
        print("Student not found.")

# Usage example
sms = StudentManagementSystem()
sms.add_student(1, "John Doe", 20, "A")
sms.add_student(2, "Jane Smith", 22, "B")
sms.add_student(3, "Michael Johnson", 21, "C")

sms.display_all_students()

sms.search_student(2)

sms.remove_student(1)

sms.display_all_students()