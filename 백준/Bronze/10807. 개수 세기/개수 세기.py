N = int(input())  # 첫째 줄: 정수의 개수 입력
numbers = list(map(int, input().split()))  # 둘째 줄: 정수 리스트 입력
v = int(input())  # 셋째 줄: 찾으려는 정수 입력

print(numbers.count(v))  # v가 리스트에 몇 번 등장하는지 출력