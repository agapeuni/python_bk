# 모듈을 읽어 들입니다.
import os

# 기본 정보를 몇 개 출력해 봅시다.
print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능].
os.mkdir("hello")
os.rmdir("hello")

# 파일을 생성하고 + 파일 이름을 변경합니다.
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일을 제거합니다.
os.remove("new.txt")
# os.unlink("new.txt")

# 시스템 명령어 실행
os.system("dir")

# 현재 폴더의 파일/폴더를 출력합니다.
output = os.listdir(".")
print("os.listdir():", output)
print()

# 현재 폴더의 파일/폴더를 구분합니다.
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)


# 폴더를 읽어 들이는 함수
def read_folder(path):
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            # 폴더라면 계속 읽어 들이기
            read_folder(item)
        else:
            # 파일이라면 출력하기
            print("파일:", item)


# 현재 폴더의 파일/폴더를 출력합니다.
read_folder(".")
