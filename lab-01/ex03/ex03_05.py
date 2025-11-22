def dem_so_lan_xuat_hien (lst, x):
    
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

#nhập danh sách từ người dùng
input_String = input ("Nhập danh sách các từ , cách nhau bởi dấu cách: ")
