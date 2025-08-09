import sys

while True:
    n = int(sys.stdin.readline())  # 한 줄씩 입력 받기
    if n == -1:  # -1이면 종료
        break

    # n의 약수(자기 자신 제외) 구하기
    divisors = [i for i in range(1, n) if n % i == 0]

    # 약수 합이 n과 같은지 확인
    if sum(divisors) == n:
        # 완전수이면 형식에 맞춰 출력
        print(f"{n} = " + " + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")
