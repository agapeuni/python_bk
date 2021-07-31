# format() 함수로 숫자를 문자열로 변환하기
string_a = "{}".format(10)
print(string_a)

# format() 함수로 숫자를 문자열로 변환하기
print("{}만 원".format(5000))
print("{} {} {}".format(3000, 4000, 5000))
print("{} {} {}".format(1, "문자열", True))

# 기본출력
print("# 기본출력")
print("{:d}".format(52))

# 특정 칸에 출력하기
print("# 특정 칸에 출력하기")
print("{:5d}".format(52))
print("{:10d}".format(52))

s = " Hello "
print(s)
print(s.strip())
