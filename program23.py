n = input('Enter a text of numbers: ')
list = n.split()
print(list)
sum = 0
for x in list:
    sum += int(x)
print(sum)

numOfWord = 0
numOfDigit = 0
numOfLetters = 0
count = 0
sentence = input("Enter a sentence: ")
length = len(sentence)
for x in sentence:
    count += 1
    x = x.lower()
    if 'a' <= x <= 'z':
        numOfLetters += 1
    elif '0' <= x <= '9':
        numOfDigit += 1
    elif count != length:
        if x == ' ' and sentence[count] != ' ':
            numOfWord += 1
print(numOfWord+1)
print(numOfDigit)
print(numOfLetters)