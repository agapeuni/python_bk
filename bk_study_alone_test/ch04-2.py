dictionary = {
    "name": "Kim",
    "head": "Black",
    "body": "Fat"
    }

print(dictionary["name"])

dictionary["name"] = "Lee"
print(dictionary)

dictionary["meta"] = "Meta"
print(dictionary)

del dictionary["name"]
print(dictionary)

for key in dictionary:
    print(key, dictionary[key])
