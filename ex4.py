file_name = input("Enter a file name: ")
email_counts = {}

try:
    # Xây dựng từ điển đếm
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith("From "):
                words = line.split()
                if len(words) > 1:
                    email_address = words[1]
                    email_counts[email_address] = email_counts.get(email_address, 0) + 1

    # Tìm giá trị lớn nhất
    largest_count = -1
    most_frequent_sender = None

    for email, count in email_counts.items():
        if count > largest_count:
            largest_count = count
            most_frequent_sender = email

    # In kết quả
    print(most_frequent_sender, largest_count)

except FileNotFoundError:
    print(f"File cannot be opened: {file_name}")