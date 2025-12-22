student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]  # Get the actual score

    if score >= 91:
        student_grades[student] = "outstanding"
    elif score >= 81:
        student_grades[student] = "exceeds expectations"
    elif score >= 71:
        student_grades[student] = "acceptable"
    else:
        student_grades[student] = "fail"

print(student_grades)