import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

# N개만 받도록 슬라이싱 (혹시 더 들어와도 N개까지만 사용)
scores = scores[:N]

MAX = max(scores)
new_scores = [(score / MAX) * 100 for score in scores]
AVG = sum(new_scores) / N

print(AVG)
