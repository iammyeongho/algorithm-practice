import sys
white = list(map(int, sys.stdin.readline().split()))
correct = [1, 1, 2, 2, 2, 8]

result = [c - w for c, w in zip(correct, white)]

print(*result)