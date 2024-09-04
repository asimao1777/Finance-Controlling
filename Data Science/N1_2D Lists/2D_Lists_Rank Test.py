import statistics

grades = [['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
          ['Thorny', '100', '90', '80'],
          ['Mac', '88', '99', '111'],
          ['Farva', '45', '56', '67'],
          ['Rabbit', '59', '61', '67'],
          ['Ursula', '73', '79', '83'],
          ['Foster', '89', '97', '101']]

# Create a dictionary that maps sutdent to grades
# Regular Long Form

avg_grades_by_student = {}

k = []
sub_ks = []

# Students' names

for i in grades:
    for j in range(len(i)):
        if j == 0 and i[j] != 'Student':
            stu = i[j]
            k.append(stu)
# print(k)

# Grades per Exam

sub_ks = list(grades[0])
sub_ks.remove(sub_ks[0])
# print(sub_ks)

new_grades = grades[1:].copy()
# print(new_grades)


# Final Dictionary with Student per Exam per Grade

for i in new_grades:
    for j in range(len(i)):
        if i[j] in k:
            avg_grades_by_student[i[j]] = round(statistics.mean([int(
                i[j+1]), int(i[j+2]), int(i[j+3])]), 0)


pre_rank = {k: v for k, v in sorted(
    avg_grades_by_student.items(), key=lambda item: item[1], reverse=True)}

print(pre_rank)


rank = []
for k in pre_rank.keys():
    rank.append(k)
print(rank)
