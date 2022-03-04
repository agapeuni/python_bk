###################################
# File Name : enumerate.py
###################################
#!/usr/bin/python3

LIST = ["A", "B", "C", "D", "E", "F"]

for item in enumerate(LIST):
    print(item)

print()
for index, value in enumerate(LIST, start=1):
    print ("%d : %s" % (index, value))

print()
for (idx, value) in enumerate(LIST, start=11):
    print('index: {}, value: {}'.format(idx, value))