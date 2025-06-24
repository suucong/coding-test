score_standard = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

sum_of_credits = 0
sum_of_grades = 0

for _ in range(20):
    grade = input().split()
    if grade[2] != 'P':
        sum_of_credits += float(grade[1])
        sum_of_grades += float(grade[1]) * score_standard[grade[2]]

print(sum_of_grades / sum_of_credits)
