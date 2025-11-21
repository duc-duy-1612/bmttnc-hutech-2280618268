# Hãy phát triển một chương trình để nhập vào một chuỗi các số nhị phân 
# với 4 chữ số, phân cách bằng dấu phẩy. Chương trình sẽ kiểm tra từng số để xác 
# định xem chúng có chia hết cho 5 hay không, sau đó in ra những số thỏa mãn điều 
# kiện này, cũng được phân tách bằng dấu phẩy. Ví dụ, nếu đầu vào là: ‘0100’, 
# ‘0011’, ‘1010’, ‘1001’, thì kết quả đầu ra sẽ là: ‘1010’

# Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chia_het_cho_5(so_nhi_phan):
    # Chuyển số nhị phân sang số thập phân
    # int(string, base) chuyển đổi chuỗi 'string' từ hệ cơ số 'base' sang hệ thập phân.
    so_thap_phan = int(so_nhi_phan, 2)
    
    # Kiểm tra xem số thập phân có chia hết cho 5 không
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False

# Nhập chuỗi số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")

# Tách chuỗi thành các số nhị phân và kiểm tra số chia hết cho 5
# Tạo một list mới (so_chia_het_cho_5) chỉ chứa các số nhị phân thỏa mãn hàm chia_het_cho_5
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

# In ra các số nhị phân chia hết cho 5
if len(so_chia_het_cho_5) > 0:
    # Nối các phần tử trong list lại thành một chuỗi, phân cách bằng dấu phẩy
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")