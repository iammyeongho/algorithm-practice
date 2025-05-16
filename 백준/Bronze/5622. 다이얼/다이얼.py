import sys
word = sys.stdin.readline().strip().upper()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
total_time = 0

for char in word:
    for idx, letters in enumerate(dial):
        if char in letters:
            total_time += (idx + 3)
            break

print(total_time)