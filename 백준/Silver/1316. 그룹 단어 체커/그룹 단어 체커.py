import sys

def is_group_word(word):
    visited = set()  # 이미 등장한 문자를 저장할 집합
    prev = ''        # 이전 문자를 저장
    for ch in word:
        # 이전 문자와 다를 때(문자가 바뀔 때)
        if ch != prev:
            # 이미 등장한 문자라면 그룹 단어가 아님
            if ch in visited:
                return False
            visited.add(ch)  # 처음 등장한 문자라면 집합에 추가
            prev = ch        # 이전 문자 갱신
    return True  # 끝까지 문제 없으면 그룹 단어

N = int(sys.stdin.readline())
count = 0  # 그룹 단어 개수 카운트

for _ in range(N):
    word = sys.stdin.readline().strip()
    if is_group_word(word):  # 그룹 단어라면
        count += 1

print(count)