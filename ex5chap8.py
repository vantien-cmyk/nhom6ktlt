file_name = input("Enter a file name: ")
count = 0

try:
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith("From "):
                words = line.split()
                if len(words) > 1:
                    print(words[1])
                    count += 1
                
    print(f"There were {count} lines in the file with From as the first word")

except FileNotFoundError:
    print(f"File cannot be opened: {file_name}")