import sys
input = sys.stdin.readline

X = int(input())

k = 1
while (k * (k + 1)) // 2 < X:
    k += 1

# k번째 대각선에서 X번째 분수 위치가 몇 번째인지 (1부터 시작)
pos = X - (k * (k - 1)) // 2

# 대각선이 홀수일 때(1,3,5,..): 위 -> 아래로 내려가기 (분자 감소, 분모 증가)
# 대각선이 짝수일 때(2,4,6,..): 아래 -> 위로 올라가기 (분자 증가, 분모 감소)
if k % 2 == 0: 
    numerator = pos
    denominator = k - pos + 1
else:
    numerator = k - pos + 1
    denominator = pos

print(f"{numerator}/{denominator}")
