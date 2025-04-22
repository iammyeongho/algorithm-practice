year = int(input())  # 연도를 입력받아 정수로 변환

# 윤년 판별 조건
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)  # 윤년이면 1 출력
else:
    print(0)  # 아니면 0 출력