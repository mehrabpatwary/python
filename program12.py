# and operator
num1 = 20
num2 = 60
num3 = 40

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# OR Operator
# Vowel = a, e, i, o, u
ch = 'b'
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")
