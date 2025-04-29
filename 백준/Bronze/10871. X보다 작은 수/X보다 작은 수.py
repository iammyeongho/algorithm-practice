N, X = map(int, input().split())     # 첫 줄에 N, X 입력
arr = list(map(int, input().split()))  # 다음 줄에 N개의 정수 입력

for num in arr:
    if num < X:
        print(num, end=' ')