###################################
# File Name : args_kwargs.py
###################################
#!/usr/bin/python3

def print_list(*args):
    for item in args:
        print("%s" % item)


def print_dict(**kwargs):
    for keyword, value in kwargs.items():
        print("keyword : %s, value : %s" % (keyword, value))


print("= List =")
list = ["A", "B", "C", "D"]
print_list(*list)

print("= Dict =")
dict = {"A": "one", "B": "two", "C": "three", "D": "four"}
print_dict(**dict)
