grades = [['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
          ['Thorny', '100', '90', '80'],
          ['Mac', '88', '99', '111'],
          ['Farva', '45', '56', '67'],
          ['Rabbit', '59', '61', '67'],
          ['Ursula', '73', '79', '83'],
          ['Foster', '89', '97', '101']]

# Create a list of the Students' names only

students = []
for i in grades:
    # print(i)
    for j in range(len(i)):
        if j == 0 and i[j] != 'Student':
            #print(i[j], type(i[j]))
            stud = i[j]
            students.append(stud)
print(students)

# Create a list only with the Exams' names from the Grade's List

assignments = list(grades[0])
assignments.remove(assignments[0])
print(assignments)
