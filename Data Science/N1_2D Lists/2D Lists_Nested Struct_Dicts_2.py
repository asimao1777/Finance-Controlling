grades = [['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
          ['Thorny', '100', '90', '80'],
          ['Mac', '88', '99', '111'],
          ['Farva', '45', '56', '67'],
          ['Rabbit', '59', '61', '67'],
          ['Ursula', '73', '79', '83'],
          ['Foster', '89', '97', '101']]

# Create a dictionary that maps sutdent to grades
# Regular Long Form

grade_dicts = {}

k = []
sub_ks = []
for i in grades:
    for j in range(len(i)):
        if j == 0 and i[j] != 'Student':
            stu = i[j]
            k.append(stu)
# print(k)

sub_ks = list(grades[0])
sub_ks.remove(sub_ks[0])
# print(sub_ks)

new_grades = grades[1:].copy()
# print(new_grades)

for i in new_grades:
    for j in range(len(i)):
        if i[j] in k:
            grade_dicts[i[j]] = {sub_ks[j]: int(
                i[j+1]), sub_ks[j+1]: int(i[j+2]), sub_ks[j+2]: int(i[j+3])}

print(grade_dicts)
