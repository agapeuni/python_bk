try:
    print("try")
    f = open("bk_pythonic/02/test_file.txt", "r")
except:
    print("except")
else:
    print("else")
    print(f.read())
    f.close()
finally:
    print("finally")

print()
try:
    print("try")
    f = open("bk_pythonic/02/not_file.txt", "r")
except:
    print("except")
else:
    print("else")
    print(f.read())
    f.close()
finally:
    print("finally")