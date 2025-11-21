def tinh_tong_so_chan (lst) :
    tong = 0
    for so in lst:
        if so % 2 == 0:
            tong += so
    return tong

# Nhập danh sách số từ người dùng và xử lý chuỗi 

input_list = input (" nhập danh sách số, cách nhau bởi dấu phẩy: ")
numbers = list ( map ( int , input_list.split ( ',' ) ) )

# sử dụng hàm và in kết quả

tong_chan = tinh_tong_so_chan ( numbers )
print ( " Tổng các số chẵn trong danh sách là: " , tong_chan )
