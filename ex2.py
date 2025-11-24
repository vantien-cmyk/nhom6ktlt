file_name = input("Enter a file name: ")
day_counts = {}

try:
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith("From "):
                words = line.split()
                if len(words) > 2:
                    day = words[2]
                    day_counts[day] = day_counts.get(day, 0) + 1

    print(day_counts)

except FileNotFoundError:
    print(f"File cannot be opened: {file_name}")