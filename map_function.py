def square(x):
    return x * x


num = [1, 2, 3, 4, 5]
print(list(map(square, num)))

# filter

result = filter(lambda x: x % 2 == 0, num)  # If condition is not matched it will remove the value for the list
print(list(result))
