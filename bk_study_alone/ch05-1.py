def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += 1

    return output


print(sum_all())
print(sum_all(1, 100, 10))
print(sum_all(end=10))
print(sum_all(end=100, step=3))


dict1 = {
    1: 1,
    2: 2
}


def fibonacci(n):
    if n in dict1:
        return dict1[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dict1[n] = output
        return output


print(fibonacci(10))
print(fibonacci(20))
print(fibonacci(30))
print(fibonacci(100))

print(dict1)
