import sys

for line in sys.stdin:  # 입력이 끝날 때까지 한 줄씩 읽음
    A, B = map(int, line.split())  # 공백으로 나눈 뒤 정수로 변환
    print(A + B)  # 두 수의 합 출력
