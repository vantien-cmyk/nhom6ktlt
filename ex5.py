file_name = input("Enter a file name: ")
domain_counts = {}

try:
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith("From "):
                words = line.split()
                if len(words) > 1:
                    email_address = words[1]
                    try:
                        domain = email_address.split('@')[1]
                    except IndexError:
                        continue
                    
                    domain_counts[domain] = domain_counts.get(domain, 0) + 1

    print(domain_counts)

except FileNotFoundError:
    print(f"File cannot be opened: {file_name}")