while True:
    sides = list(map(int, input().split()))
    if sides == [0, 0, 0]:
        break

    a, b, c = sorted(sides)
    # 삼각형의 조건 : 가장 긴 변 < 나머지 두 변의 합
    if a + b <= c:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
