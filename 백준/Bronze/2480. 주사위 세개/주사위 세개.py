# 주사위 3개의 눈 입력받기
dice = list(map(int, input().split()))
a, b, c = sorted(dice)  # 오름차순 정렬

# 조건에 따른 상금 계산
if a == b == c:  # 모두 같은 경우
    print(10000 + a * 1000)
elif a == b or b == c:  # 2개만 같은 경우 (정렬로 인해 b가 항상 공통값)
    print(1000 + b * 100)
else:  # 모두 다른 경우 (정렬로 인해 c가 최대값)
    print(c * 100)