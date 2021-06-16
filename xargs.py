# xarg
def student(*details):  # Tuples
    print(details[1])


student(101, 'Mehrab Patwary', 3.56)


def add(*number):
    sum = 0
    for x in number:
        sum += x
    print(sum)


add(12, 15, 16)
add(12, 15)
