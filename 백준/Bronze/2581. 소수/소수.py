import sys

# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1): # 제곱근까지 확인
        if num % i == 0:
            return False
    return True

# 입력 받기
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

primes = [x for x in range(M, N+1) if is_prime(x)] # 구간 내 소수 찾기

if primes:
    print(sum(primes)) # 소수의 합 출력
    print(min(primes)) # 소수 중 최솟값 출력
else:
    print(-1) # 소수가 없으면 -1 출력
