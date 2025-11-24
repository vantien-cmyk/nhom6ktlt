fname = input("Enter the file name: ")

# Easter Egg đặc biệt
if fname.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

# Thử mở file
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0

# Đếm số dòng bắt đầu bằng "Subject:"
for line in fhand:
    if line.startswith("Subject:"):
        count += 1

print("There were", count, "subject lines in", fname)
