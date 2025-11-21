# - Câu 10: Viết một hàm nhận vào một chuỗi và trả về chuỗi đảo ngược của nó

def dao_nguoc_chuoi(chuoi):
   
    return chuoi[::-1]

# Sử dụng hàm và in kết quả
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))
