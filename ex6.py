text = 'X-DSPAM-Confidence:0.8475'
# Tìm vị trí dấu hai chấm
colon_pos = text.find(':')
# Cắt chuỗi sau dấu hai chấm
num_str = text[colon_pos + 1:]
# Chuyển thành số thực
value = float(num_str)
print(value)

