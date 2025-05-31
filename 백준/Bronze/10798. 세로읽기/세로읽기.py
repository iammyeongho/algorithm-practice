import sys

words = [sys.stdin.readline().strip() for _ in range(5)]
result = ''

# 각 줄의 최대 길이(최대 15글자)
for col in range(15):
    for row in range(5):
        if col < len(words[row]):
            result += words[row][col]

print(result)