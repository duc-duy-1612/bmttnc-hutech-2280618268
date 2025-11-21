so_gio_lam = float (input ("nhap so gio lam moi tuan : "))
luong_gio = float (input ("nhap thù lao trên mỗi giờ làm tiêu chuẩn : "))
gio_tieu_chuan = 44 # số giờ làm chuẩn mỗi tuần 
gio_vuot_chuan = max ( 0 , so_gio_lam - gio_tieu_chuan) # số giờ làm vượt chuẩn mỗi tuần 
thuc_linh= gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5 # tính tổng thu nhập 
print (f"số tiền thực lĩnh của nhân viên : {thuc_linh} ")