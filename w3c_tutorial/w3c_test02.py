quantity = 3
itemno = 567
price = 49.95

myorder1 = "I want {} pieces of item {} for {} dollars."
print(myorder1.format(quantity, itemno, price))

myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder2.format(quantity, itemno, price))

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})