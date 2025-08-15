import sys

# 소수 판별 함수
def is_prime(num):
    if num < 2:  # 2 미만은 소수가 아님
        return False
    for i in range(2, int(num ** 0.5) + 1):  # 제곱근까지만 검사
        if num % i == 0:
            return False
    return True

# 입력 받기
N = int(sys.stdin.readline())  # 수의 개수
numbers = list(map(int, sys.stdin.readline().split()))

# 소수 개수 세기
count = sum(1 for num in numbers if is_prime(num))

# 결과 출력
print(count)
