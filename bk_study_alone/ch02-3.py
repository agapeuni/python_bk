# 변수 선언과 할당
pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2 * pi * r)  # 원의 둘레
print("원의 넓이 =", pi * r * r)  # 원의 넓이

a = 10
a = a + 5
a = a + 5
print(a)

a += 5
print(a)

a -= 5
print(a)

v = input("값을 입력하세요.")
print(type(v))

input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)
