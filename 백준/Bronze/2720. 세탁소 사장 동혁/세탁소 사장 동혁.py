import sys

how_many = int(sys.stdin.readline())  # 테스트 케이스 개수

for _ in range(how_many):
    change = int(sys.stdin.readline())  # 거스름돈(센트)
    q = change // 25                   # 쿼터 개수
    change_left = change % 25           # 남은 거스름돈
    d = change_left // 10               # 다임 개수
    change_left = change_left % 10      # 남은 거스름돈
    n = change_left // 5                # 니켈 개수
    p = change_left % 5                 # 페니 개수
    print(q, d, n, p)