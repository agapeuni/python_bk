filename = '_FileTest.txt'

print("@@ readline")
with open(filename, mode='r') as f1:
    print(f1.readline())
    print(f1.readline())

print("@@ write w")
with open(filename, mode='w') as f2:
    f2.write('Hello Python')

print("@@ write a+")
with open(filename, mode='a+') as f3:
    f3.write('\nHello Python (Append)')

print("@@ for line")
with open(filename) as f4:
    for line in f4:
        print(line)
