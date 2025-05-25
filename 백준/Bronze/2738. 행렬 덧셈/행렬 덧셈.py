import sys

# 행렬 크기 입력
N, M = map(int, sys.stdin.readline().split())

# 행렬 A 입력
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 행렬 B 입력
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 행렬 합 계산 및 출력
for i in range(N):
    result = []
    for j in range(M):
        result.append(A[i][j] + B[i][j])
    print(*result)