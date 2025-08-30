import sys

# 입력: 세 점
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(3)]

# x, y 좌표 각각 따로 저장
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

# 세 점 중 두 번 등장하는 값은 변이고, 한 번만 등장하는 값이 네 번째 점의 좌표가 됨
for_x = [x for x in x_vals if x_vals.count(x) == 1][0]
for_y = [y for y in y_vals if y_vals.count(y) == 1][0]

print(for_x, for_y)
