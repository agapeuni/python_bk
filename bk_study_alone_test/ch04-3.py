# for 반복문과 범위를 함께 조합해서 사용합니다.
for i in range(5):
    print(str(i) + "= 반복 변수")
print()

for i in range(5, 10):
    print(str(i) + "= 반복 변수")
print()

for i in range(0, 15, 3):
    print(str(i) + "= 반복 변수")
print()

print(list(range(10)))

# 역반복문
for i in reversed(range(5)):
    # 출력합니다.
    print("현재 반복 변수: {}".format(i))

# 반복 변수를 기반으로 반복하기
i = 0
while i < 5:
    print("{}번째 반복입니다.".format(i))
    i += 1

# 변수를 선언합니다.
list_test = [1, 2, 1, 2]
value = 2

# list_test 내부 value 반복
while value in list_test:
    list_test.remove(value)

# 출력합니다.
print(list_test)
