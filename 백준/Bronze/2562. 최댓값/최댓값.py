import sys

arr = []
for _ in range(9):
    num = int(sys.stdin.readline())
    arr.append(num)

print(max(arr))
print(arr.index(max(arr)) + 1)