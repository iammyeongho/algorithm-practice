import sys

# 9x9 격자판 입력
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max_value = -1
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if grid[i][j] > max_value:
            max_value = grid[i][j]
            max_row, max_col = i, j

print(max_value)
print(max_row + 1, max_col + 1)