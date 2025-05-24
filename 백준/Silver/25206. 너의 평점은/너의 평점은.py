import sys

grade_score = {
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

total_score = 0.0  # (학점 × 평점) 누적합
total_credit = 0.0 # 학점 누적합

for _ in range(20):
    line = sys.stdin.readline().strip()
    subject, credit, grade = line.split()
    credit = float(credit)
    if grade == 'P':
        continue  # P는 계산에서 제외
    total_score += credit * grade_score[grade]
    total_credit += credit

print(total_score / total_credit)