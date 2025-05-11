import sys

A = set()
for _ in range(10):
    num = int(sys.stdin.readline().rstrip())
    A.add(num % 42)
print(len(A))
