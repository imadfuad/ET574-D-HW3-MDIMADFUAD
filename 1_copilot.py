# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
students.append("Sara")
students.append("Miko") 
# change Jon to John
students[0] = 'John'
def greet_students(students): 
    for student in students: 
        print(f"Hello, {student}!")
greet_students(students) 
print("Total students:", len(students))
 
