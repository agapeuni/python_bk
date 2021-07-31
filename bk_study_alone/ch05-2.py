print("lambda")
print((lambda x, y: x + y)(10, 20))
print(map(lambda x: x ** 2, range(5)))
print(list(map(lambda x: x ** 2, range(5))))


list1 = [1, 2, 3, 4, 5]
out1 = map(lambda x: x * x, list1)

print(out1)
print(list(out1))

out2 = filter(lambda x: x < 3, list1)
print(out2)
print(list(out2))
