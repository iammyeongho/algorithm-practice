import sys

paper = [[0]*100 for _ in range(100)] # 도화지 배열

N = int(sys.stdin.readline()) # 색종이 개수

for _ in range(N):
    # 색종이의 왼쪽 아래 좌표 입력
    x, y = map(int, sys.stdin.readline().split())

    # 색종이 크기는 10x10이므로, (x, y)부터 (x+9, y+9)까지 덮음
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1 # 색종이가 붙은 부분을 1로 표시

# 색종이가 붙은 모든 칸(1로 표시된 칸)의 개수를 셈
area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1 # 색종이가 차지하는 칸을 카운트

print(area) # 최종 넓이(색종이가 차지하는 전체 면적) 출력