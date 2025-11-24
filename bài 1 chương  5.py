total = 0.0
count = 0

while True:
    s = input("Enter a number: ")
    if s.lower() == "done":
        break
    try:
        num = float(s)
    except:
        print("Invalid input")
        continue
    total += num
    count += 1

if count == 0:
    print("No numbers were entered.")
else:
    average = total / count
    print(total, count, average)