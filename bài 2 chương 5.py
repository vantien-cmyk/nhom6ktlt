max = None
min = None

while True:
    entry = input("Enter a number: ")
    if entry.lower() == "done":
        break
    try:
        num = float(entry)
    except:
        print("Invalid input")
        continue

    if max is None or num > max:
        max = num
    if min is None or num < min:
        min = num

if max is None:
    print("No numbers were entered.")
else:
    def pretty(x):
        return int(x) if x == int(x) else x
    print("Maximum:", pretty(max))
    print("Minimum:", pretty(min))