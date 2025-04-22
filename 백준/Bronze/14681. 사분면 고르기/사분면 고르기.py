x = int(input())  # x좌표 입력
y = int(input())  # y좌표 입력

# 사분면 판별
if x > 0 and y > 0:
    print(1)  # 제1사분면
elif x < 0 and y > 0:
    print(2)  # 제2사분면
elif x < 0 and y < 0:
    print(3)  # 제3사분면
else:
    print(4)  # 제4사분면
