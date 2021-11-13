thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
  print(x)
  
thisset.add("orange")
print(thisset)

thisset.update(["orange", "mango", "apple"])
print(thisset)


thisset.remove("orange")
print(thisset)

set1 = {"a", "b" , "c"}
print(set1.union(thisset))

set2 = {1, 2, 3}

set1.update(set2)
print(set1)