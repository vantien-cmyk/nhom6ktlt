name = input("Enter a file name: ")

try:
    fhand = open(name)
except:
    print("File cannot be opened:", name)
    quit()

for line in fhand:
    line = line.rstrip()
    print(line.upper())
