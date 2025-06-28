grades = {'John': [85, 90, 88], 'Alice': [75, 80, 82], 'Bob': [92, 88, 90]}
for student, marks in grades.items():
    avg = sum(marks) / len(marks)
    print(f"{student}: {avg:.2f}")
