import sys
A, B = sys.stdin.readline().split()
A_R = int(A[::-1])
B_R = int(B[::-1])
print(max(A_R,B_R))