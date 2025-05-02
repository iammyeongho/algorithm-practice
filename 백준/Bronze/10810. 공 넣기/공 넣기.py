import sys

N, M = map(int, sys.stdin.readline().split())

baskets = [0] * (N + 1)  # 인덱스 1부터 N까지 사용

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    # i번부터 j번 바구니까지 k번 공으로 채우기
    for idx in range(i, j + 1):
        baskets[idx] = k

# 1번 바구니부터 N번까지 출력
print(' '.join(map(str, baskets[1:N+1])))
