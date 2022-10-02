# 1
name = input("enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
out_file = open("name.txt")
text = out_file.read()
out_file.close()
print(text)


# 3
total = 0
out_file = open("numbers.txt", "r")
for line in out_file:
    total += float(line)
    print(total)
out_file.close()


# 4
total = 0
out_file = open("numbers.txt", "r")
for line in out_file:
    total += float(line)
    print(total)
out_file.close()