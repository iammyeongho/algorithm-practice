import sys

S = sys.stdin.readline().strip()
result = []

# 알파벳 'a'부터 'z'까지 직접 탐색
for code in range(ord('a'), ord('z')+1):
    ch = chr(code)
    found = -1  # 기본값: -1 (없으면 -1)
    for idx in range(len(S)):
        if S[idx] == ch:
            found = idx  # 처음 등장하면 인덱스 저장
            break        # 첫 등장만 찾으면 되므로 종료
    result.append(str(found))

print(' '.join(result))