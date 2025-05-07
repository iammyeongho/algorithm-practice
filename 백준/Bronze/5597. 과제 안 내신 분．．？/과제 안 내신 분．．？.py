import sys

numbers = [int(sys.stdin.readline()) for _ in range(28)]

all = set(range(1, 31))

submit = set(numbers)

# 제출하지 않은 학생 찾기 (정렬 후 출력)
not_submit = sorted(all - submit)

print(not_submit[0])
print(not_submit[1])