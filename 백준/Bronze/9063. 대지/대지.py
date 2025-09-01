import sys

N = int(sys.stdin.readline())
min_x = 10000
max_x = -10000
min_y = 10000
max_y = -10000

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

# 넓이 계산
print((max_x - min_x) * (max_y - min_y))
