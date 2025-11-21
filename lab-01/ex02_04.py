# tao 1 danh sach rỗng để lưu kết quả 
j = [] 

# duyệt qua tất cả các số trong đoạn từ 2000 - 3200 
# kt xem số i có chia đc hết cho 7 và kphai là bội số của 5 ko 

for i in range ( 2000 , 3201 ) :
    if ( i % 7 == 0 ) and ( i % 5 != 0 ) :
        j.append(str(i))
print (",".join(j))

