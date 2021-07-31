list1 = [11, 12, 13, 14]
print(min(list1), max(list1), sum(list1))

# 제너레이터
list2 = reversed(list1)
print(list2)
print(list(list2))

for i in reversed(list1):
    print(i)

# 변수를 선언합니다.
example_dictionary = {
    "키A": "값A",
    "키B": "값B"
}

# 딕셔너리의 items() 함수 결과 출력하기
print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

# for 반복문과 items() 함수 조합해서 사용하기
print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, value in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, value))

# 변수를 선언합니다.
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

# reversed_numbers 출력
print("reversed_numbers :", r_num)
print(next(r_num))
print(next(r_num))
