import sys  # 표준 입력을 빠르게 받기 위해 sys 모듈 사용

T = int(sys.stdin.readline())

for _ in range(T):  # T번 반복하면서 처리
    A, B = map(int, sys.stdin.readline().split())  # 한 줄에서 두 정수 A, B를 입력받아 정수로 변환
    print(A + B)  # 두 수의 합을 출력
