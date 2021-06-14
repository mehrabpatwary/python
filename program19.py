num = [10, 20, 30, 40, 50]
print(num)

"""
index = 0
n = len(num)
while index < n:
    print(num[index])
    index += 1
"""
sum = 0
for x in num:
    sum += x
    print(x)
    
print(sum)