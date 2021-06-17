file = open('student.txt', "r+")  # r, w, r+

print(file.readable())
print(file.writable())

# text = file.read()
# print(text)
# print(len(text))

# text = file.readlines()[2]  # text = file.readlines()
# print(text)

for line in file:
    print(line)

file.close()