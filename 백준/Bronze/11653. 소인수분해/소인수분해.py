import sys

N = int(sys.stdin.readline()) # 입력 받기

n = N
factor = 2 # 소인수 후보 (처음은 2부터)

while factor <= n:
    # 소인수인 경우
    while n % factor == 0:
        print(factor)
        n //= factor # N을 나누어 갱신
    factor += 1 # 다음 소인수 후보로 이동
