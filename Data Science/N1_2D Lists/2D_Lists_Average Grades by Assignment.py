import statistics

grades = [['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
          ['Thorny', '100', '90', '80'],
          ['Mac', '88', '99', '111'],
          ['Farva', '45', '56', '67'],
          ['Rabbit', '59', '61', '67'],
          ['Ursula', '73', '79', '83'],
          ['Foster', '89', '97', '101']]

avg_grades_by_assignment = {}
avg_grades_by_assignment[grades[0][1]] = statistics.mean(
    [int(a[1]) for a in grades[1:]])
avg_grades_by_assignment[grades[0][2]] = statistics.mean(
    [int(a[2]) for a in grades[1:]])
avg_grades_by_assignment[grades[0][3]] = statistics.mean(
    [int(a[3]) for a in grades[1:]])

print(avg_grades_by_assignment)
