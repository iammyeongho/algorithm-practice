X = int(input())
N = int(input())

total = 0

# 이후 N개의 줄: 각 물건의 가격 a와 개수 b 입력
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b

# 계산한 총 금액과 영수증 금액이 일치하는지 출력
if total == X:
    print("Yes")
else:
    print("No")
