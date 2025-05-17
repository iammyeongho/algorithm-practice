import sys

# 모든 입력 줄을 리스트로 저장 (최대 100줄)
lines = [line.rstrip('\n') for line in sys.stdin]

for line in lines:
    print(line)