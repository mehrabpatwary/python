file = open("student.txt",'a')  # a means append file, add new line on old file. 'w' means old file clear new line added

file.write("\n11 Mehrab Patwary")

file1 = open("student1.html", 'a')  # New file will be added
file1.write('<h1>This is a header file</h1>')

file.close()
