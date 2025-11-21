print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []

while True:
    line = input()
    # Kiểm tra điều kiện kết thúc
    if line.lower() == 'done':
        break
    # Thêm dòng vào danh sách nếu không phải là 'done'
    lines.append(line)

print("\nCác dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())