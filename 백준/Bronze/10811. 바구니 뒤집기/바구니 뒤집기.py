import sys

N, M = map(int, sys.stdin.readline().split())
baskets = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    # i-1부터 j까지 슬라이싱 → 역순으로 교체
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(' '.join(map(str, baskets)))
