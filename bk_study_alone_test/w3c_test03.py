thislist = ["apple", "banana", "cherry"]

thislist.append("orange")
print(thislist)

thislist.insert(1, "pineapple")
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

list = ["a", "b" , "c"]
thislist.extend(list)
print(thislist)

print(tuple(thislist))