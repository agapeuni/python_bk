import random

name1 = "김이박최소"
name2 = list("가나다라마바사아자차카타파하")

for i in range(10):
    name = random.choice(name1) + random.choice(name2) + random.choice(name2)
    weight = random.randrange(60, 80)
    height = random.randrange(160, 180)
    print("{} {} {}".format(name, weight, height))

