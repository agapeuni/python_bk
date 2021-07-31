# 숫자를 입력받습니다.
user_input_a = input("정수 입력> ")

# 사용자 입력이 숫자로만 구성되어 있을 때
if user_input_a.isdigit():
    # 숫자로 변환합니다.
    number_input_a = int(user_input_a)
    # 출력합니다.
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다.")

# try except 구문으로 예외를 처리합니다.
try:
    # 숫자로 변환합니다.
    number_input_b = int(input("정수 입력> "))
    # 출력합니다.
    print("원의 반지름:", number_input_b)
    print("원의 둘레:", 2 * 3.14 * number_input_b)
    print("원의 넓이:", 3.14 * number_input_b * number_input_b)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")
