file_name = "romeo.txt"
try:
    with open(file_name, 'r') as f:
        words_set = set(word for line in f for word in line.rstrip().split())
    
    unique_words_sorted = sorted(list(words_set))
    print(unique_words_sorted)

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tệp '{file_name}'.")