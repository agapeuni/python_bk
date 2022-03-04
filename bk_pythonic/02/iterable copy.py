list = ["A", "B", "C", "D", "E", "F"]
print(type(list))

for i in list:
    print(i)

iterator1 = iter(list)
print(type(iterator1))

print(next(iterator1))
print(next(iterator1))

print()
dict = {"A": "one", "B": "two", "C": "three", "D": "four"}
print(type(dict))

for d in dict:
    print(d)    

iterator2 = iter(dict)
print(type(iterator2))

print(next(iterator2))
print(next(iterator2))
