# 총감 ,부감
# 총감 = B명, 부감 = C명
# 시험장 당 총감 1, 부감 여러명
# 각 시험장마다 응시생 감시, 이에 필요한 감독관 최솟값

import sys
N = int(sys.stdin.readline()) # 시험장
A = list(map(int, sys.stdin.readline().split())) # 시험장 응시생
B, C = map(int, sys.stdin.readline().split()) # 총감 감시수, 부감 감시수

total = 0 # 감독관 수

for i in A:
    total += 1  # 총감독관
    remaining = i - B
    if remaining > 0:
        total += (remaining + C - 1) // C  # 부감독관 계산 (올림)

print(total)
