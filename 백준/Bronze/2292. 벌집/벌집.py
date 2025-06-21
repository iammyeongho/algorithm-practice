import sys

# 입력값 받기: N번 방까지 최소 몇 개의 방을 지나는지 계산
N = int(sys.stdin.readline().strip())

# 1번 방은 바로 1번이므로, 방을 1개만 지남
if N == 1:
    print(1)
else:
    # 현재 층(레이어) 번호, 1부터 시작
    layer = 1
    # 현재 층의 마지막 방 번호
    max_room = 1
    # N이 현재 층의 마지막 방 번호보다 큰 동안 반복
    while N > max_room:
        # 다음 층의 마지막 방 번호 = 이전 마지막 방 번호 + 6*층수
        max_room += 6 * layer
        # 층수 증가
        layer += 1
    print(layer)
