a, b, c = map(int, input().split())
sides = sorted([a, b, c])

# 삼각형 조건: 최대 변 길이 < 나머지 두 변의 합이어야 함
if sides[2] < sides[0] + sides[1]:
    print(sum(sides))
else:
    # 가장 긴 변을 (a + b - 1)로 줄여야 넓이가 양수인 삼각형 생성 가능
    max_perimeter = sides[0] + sides[1] + (sides[0] + sides[1] - 1)
    print(max_perimeter)
