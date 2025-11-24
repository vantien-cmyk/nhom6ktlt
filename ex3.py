file_name = input("Enter file name: ")
email_counts = {}

try:
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith("From "):
                words = line.split()
                if len(words) > 1:
                    email_address = words[1]
                    email_counts[email_address] = email_counts.get(email_address, 0) + 1

    print(email_counts)

except FileNotFoundError:
    print(f"File cannot be opened: {file_name}")