a = int(input())
b = int(input())
c = int(input())

angles = [a, b, c]

if sum(angles) != 180:
    print("Error")
else:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
