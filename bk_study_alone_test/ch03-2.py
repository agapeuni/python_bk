# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 짝수 조건
if number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

print()

a = 0
if a:
    print("0은 True로 변환됩니다")
else:
    print("0은 False로 변환됩니다")

print()

b = ""
if b:
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 변환됩니다")
