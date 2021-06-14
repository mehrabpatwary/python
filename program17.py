subject = ["C", "C++", "Java", "Python", "BASIC"]
print(len(subject))

subject.append("TOC")
print(subject)

subject.insert(2, "OS")
print(subject)

subject.sort()
print(subject)

subject.remove("BASIC")
print(subject)

num = [10, 55, 2, 888]
num.sort()
print(num)
num.reverse()
print(num)

num.pop()
num.pop()
print(num)

num.clear()
print(num)

subject2 = subject.copy()
print(subject2)

num2 = [85, 60, 60, 60, 89, 55]
pos = num2.index(89)
print(pos)
pos = num2.count(60)
print(pos)

