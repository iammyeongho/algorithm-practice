T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):  # T번 반복
    A, B = map(int, input().split())  # 각 줄에서 두 정수 입력
    print(A + B)  # 두 수의 합 출력
