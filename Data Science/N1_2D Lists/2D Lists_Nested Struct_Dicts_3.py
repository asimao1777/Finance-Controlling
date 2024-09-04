grades = [['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
          ['Thorny', '100', '90', '80'],
          ['Mac', '88', '99', '111'],
          ['Farva', '45', '56', '67'],
          ['Rabbit', '59', '61', '67'],
          ['Ursula', '73', '79', '83'],
          ['Foster', '89', '97', '101']]

grades_by_assignment = {}
grades_by_assignment[grades[0][1]] = [int(a[1]) for a in grades[1:]]
grades_by_assignment[grades[0][2]] = [int(a[2]) for a in grades[1:]]
grades_by_assignment[grades[0][3]] = [int(a[3]) for a in grades[1:]]

print(grades_by_assignment)
