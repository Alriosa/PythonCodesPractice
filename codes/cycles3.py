#Filling an array

array_students = list()
students_numbers = input("Enter the number of students")

for i in range(int(students_numbers)):
    student = input("Name: ")
    array_students.append(student)

for i in range(len(array_students)):
    print (array_students[i])

print('Student' , students_numbers)
