import sys

N = int(sys.stdin.readline())  # 숫자의 개수 입력
numbers = sys.stdin.readline().strip()  # 공백 없이 이어진 숫자 입력
total = 0
    
for i in range(N):  # N번 반복
    total += int(numbers[i])  # i번째 숫자를 정수로 변환해서 더함

print(total)
