import sys
word = sys.stdin.readline().strip()
croatian = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in croatian:
    word = word.replace(alpha, ' ')
print(len(word))