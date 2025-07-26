import sys
import math

# 입력 처리
A, B, V = map(int, sys.stdin.readline().split())

# (V - A) / (A - B)의 올림 + 1
# 마지막 날 낮에 올라가면 미끄러지지 않으므로 V - A까지 전날에 도달해야 함
days = math.ceil((V - A) / (A - B)) + 1

print(days)
