# 1 + 2 + 3 + 4 + ... + n
n = int(input('Enter the last number: '))
sum = 0

for x in range(1, n+1, 1):
    sum += x
print(sum)

# 2 + 4 + 6 + ... + n
sum = 0
for x in range(2, n+1, 2):
    sum += x
print(sum)

# 1*1 + 2*2 + 3*3 + ... + n*n
sum = 0
for x in range(1, n+1, 1):
    sum += x*x
print(sum)

# Factorial
sum = 1
for x in range(n, 1, -1):
    sum *= x

print(sum)