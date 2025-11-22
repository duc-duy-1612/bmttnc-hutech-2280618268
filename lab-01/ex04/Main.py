from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while ( 1 == 1) :
    print ("\n Chuong trình quản lý sinh viên ")
    print ("********************************** MENU **********************************")
    print ("1. Thêm sinh viên ")
    print ("2. Cập nhật sinh viên theo ID ")    
    print ("3. Xóa sinh viên theo ID ")
    print ("4. Tìm kiếm sinh viên theo ID ")
    print ("5. sắp xếp sinh viên theo điểm trung bình ")
    print ("6. sắp xếp sinh viên theo chuyên ngành ")
    print ("7. Hiển thị danh sách sinh viên ")
    print ("8. Thoát chương trình ")
    print ("**************************************************************************")
    
    key = int ( input ("Mời bạn chọn chức năng : ") )
    if key == 1 :
        print ("\n1. Thêm sinh viên ")
        qlsv.nhapSinhVien()
        print ("\n Thêm sinh viên thành công !")
        
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\nn2. Cap nhat thong tin sinh vien. ")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\nn3. Xoa sinh vien.")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh vien co id = ", ID, " da bi xoa.")
            else:
                print("\nSinh vien co id = ", ID, " khong ton tai.")
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\nn4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\nn5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 6): # Bắt đầu từ hình ảnh thứ hai
        if (qlsv.soLuongSinhVien() > 0):
            print("\nn6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\nn7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")