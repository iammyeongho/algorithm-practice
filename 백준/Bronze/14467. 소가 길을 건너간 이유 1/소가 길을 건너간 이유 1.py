import sys
N = int(sys.stdin.readline())
last_loc = {} # 소와 위치 저장
count = 0 # 겹치는 위치

for _ in range(N):
    cow, loc = map(int, sys.stdin.readline().split())
    if cow in last_loc: # 현재 소가 관찰됐는지 확인
        if last_loc[cow] != loc: # 관찰되지 않았다면 카운트 증가
            count += 1
    last_loc[cow] = loc # 현재 위치 기록

print(count)