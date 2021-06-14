n = 10

for i in range(n + 1):
    print(i * '*')

for i in range(n + 1):
    print((2 * i - 1) * '*')

j = n+1
for i in range(1, n + 1, 2):
    print(j * ' ', end='')
    print(i * '*')
    j -= 1
