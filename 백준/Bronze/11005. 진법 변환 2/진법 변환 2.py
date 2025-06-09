import sys

N, B = map(int, sys.stdin.readline().split())
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []

if N == 0:
    print(0)
else:
    while N > 0:
        result.append(digits[N % B])
        N = N // B
    print(''.join(reversed(result)))
