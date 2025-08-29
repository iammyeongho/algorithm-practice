import sys

x, y, w, h = map(int, sys.stdin.readline().split())  # 입력 받기

# 각 경계선까지의 거리 계산
to_left   = x       
# 왼쪽 경계 (x=0)까지의 거리
to_bottom = y       
# 아래쪽 경계 (y=0)까지의 거리
to_right  = w - x   
# 오른쪽 경계 (x=w)까지의 거리
to_top    = h - y   
# 위쪽 경계 (y=h)까지의 거리

# 최솟값 출력
print(min(to_left, to_bottom, to_right, to_top))
