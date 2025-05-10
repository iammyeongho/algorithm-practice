import sys

T = int(sys.stdin.readline())
for _ in range(T):
    parts = sys.stdin.readline().split()
    R = int(parts[0])
    S = ' '.join(parts[1:])  # 공백 포함 문자열 처리
    result = ''.join([char * R for char in S])
    print(result)