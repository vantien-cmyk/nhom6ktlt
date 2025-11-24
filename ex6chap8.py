numbers = []

while True:
    entry = input("Enter a number: ")
    if entry.lower() == 'done':
        break
    
    try:
        num = float(entry)
        numbers.append(num)
    except ValueError:
        print("Invalid input")
        continue

if numbers:
    print(f"Maximum: {max(numbers):.1f}")
    print(f"Minimum: {min(numbers):.1f}")
else:
    print("No numbers were entered.")