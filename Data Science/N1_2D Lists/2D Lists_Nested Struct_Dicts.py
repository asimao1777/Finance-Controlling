grades = [
    ["Student", "Exam 1", "Exam 2", "Exam 3"],
    ["Thorny", "100", "90", "80"],
    ["Mac", "88", "99", "111"],
    ["Farva", "45", "56", "67"],
    ["Rabbit", "59", "61", "67"],
    ["Ursula", "73", "79", "83"],
    ["Foster", "89", "97", "101"],
]

# Create a dictionary that maps student to grades
# Regular Long Form

grade_list = {}

k = []
for i in grades:
    for j in range(len(i)):
        if j == 0 and i[j] != "Student":
            stu = i[j]
            k.append(stu)
# print(k)

new_grades = grades[1:].copy()
# print(new_grades)

for i in new_grades:
    for j in range(len(i)):
        if i[j] in k:
            grade_list[i[j]] = [int(i[j + 1]), int(i[j + 2]), int(i[j + 3])]

print(grade_list)


# With List Compreheension

k = [[i[j] for j in range(len(i)) if j == 0 and i[j] != "Student"] for i in grades]
# print(k)
k.pop(0)
j = k.copy()
final_k = ["".join(i) for i in j]

# print(final_k)
