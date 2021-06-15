num = {1, 2, 3, 4, 5, 5}
print(num)
num2 = set([4, 5, 6])
num2.add(7)
num2.remove(7)
print(num2)
print(7 in num2)
print(7 not in num2)

num3 = set([4, 5, 6, 7])
print(num | num3)
print(num & num3)
print(num - num3)
