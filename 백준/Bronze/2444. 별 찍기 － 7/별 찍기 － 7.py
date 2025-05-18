import sys
N = int(sys.stdin.readline())
for i in range(2*N-1):
    k = N - 1 - abs(N-1 - i)
    print(' ' * (N-1 - k) + '*' * (2*k + 1))