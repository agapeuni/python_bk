list1 = ["Java", "Python", "C"]
print(list1)

list1[2] = "C++"
print(list1)

list1.append("HTML")
print(list1)

print(len(list1))

list2 = [0, 1, 2, 3, 4, 5]

list2.insert(0, 7)
list2.append(6)
print(list2)

del list2[3]
print(list2)

list2.pop()
print(list2)

list2.pop(1)
print(list2)

list2.remove(4)
print(list2)
print(len(list2))

for element in list2:
    print(element)

list1.extend(list2)
print(list1)
print(list2)
