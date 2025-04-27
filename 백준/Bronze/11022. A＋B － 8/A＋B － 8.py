T = int(input())  # 테스트케이스 개수 입력

for i in range(1, T + 1):  # 1부터 T까지 반복 (케이스 번호를 위해)
    A, B = map(int, input().split())  # 각 줄마다 A, B 입력
    C = A + B
    print(f"Case #{i}: {A} + {B} = {C}")  # 케이스 번호와 결과 출력
