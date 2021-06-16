book = []
book.append('Learn Java')
book.append('Learn C')
book.append('Learn C++')

print(book)

book.pop()
print(book)
print("Now the top book is", book[-1])
book.pop()
print(book)
book.pop()
if not book:
    print('No book left')