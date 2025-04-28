import sys

while True:
    line = sys.stdin.readline().rstrip()  # 한 줄 입력받고 개행문자 제거
    if line == "0 0":  # 종료 조건
        break
    A, B = map(int, line.split())  # 공백 기준으로 분리 후 정수 변환
    print(A + B)  # 두 수의 합 출력
