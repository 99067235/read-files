import time

file = open("C:/Users/Jurrian/Documents/Projecten/read-files/README.md", "r")

line = True

while line:
    line = file.readline()
    print(line)
    time.sleep(1)