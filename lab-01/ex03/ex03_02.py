def dao_nguoc_list(lst):
    return lst[::-1]

#Nhap danh sách từ người dùng và xử lý chuỗi

input_list = input("Nhập danh sách các phần tử, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# sỬ dụng hàm và in kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("list đảo ngược là:", list_dao_nguoc)
