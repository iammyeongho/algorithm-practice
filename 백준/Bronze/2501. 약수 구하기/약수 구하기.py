import sys

# 입력
N, K = map(int, sys.stdin.readline().split())

# 약수 찾기 (1부터 N까지)
divisors = [i for i in range(1, N + 1) if N % i == 0]

# K번째 약수 출력
if len(divisors) >= K:
    print(divisors[K - 1])  # K번째는 인덱스 K-1
else:
    print(0)