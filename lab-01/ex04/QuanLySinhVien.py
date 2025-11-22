from SinhVien import SinhVien

class QuanLySinhVien :
    listSinhVien = []
    
    def generateID (self):
        maxId = 1 
        if len (self.listSinhVien) > 0 :
            maxId = self.listSinhVien[0].id
            for sv in self.listSinhVien :
                if sv.id < maxId :
                    maxId = sv.id
            maxId += 1
        return maxId
    
    def soLuongSinhVien (self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien (self ):
        sviD = self.generateID()
        name = input ("Nhập tên sinh viên : ")
        sex = input ("Nhập giới tính sinh viên : ")
        major = input ("Nhập chuyên ngành sinh viên : ")
        diemTB = float ( input ("Nhập điểm trung bình sinh viên : ") )     
        sv = SinhVien (sviD , name , sex , major , diemTB )
        self.xepLoaiHocLuc (sv)
        self.listSinhVien.append (sv)
        
    def updateSinhVien ( self , ID ) :
        sv: SinhVien = self.findByID (ID)
        if sv != None :
            name = input ("Nhập tên sinh viên : ")
            sex = input ("Nhập giới tính sinh viên : ")
            major = input ("Nhập chuyên ngành sinh viên : ")
            diemTB = float ( input ("Nhập điểm trung bình sinh viên : ") )      
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc (sv)
        else :
            print ("Sinh viên có ID {} k tồn tại " .format (ID) )
    
    def sortByID (self):
        self.listSinhVien.sort ( key = lambda x :x.id , reverse = False )
        
    def sortByName (self):
        self.listSinhVien.sort ( key = lambda x :x.name , reverse = False )
        
    def sortByDiem (self):
        self.listSinhVien.sort ( key = lambda x :x.diemTB , reverse = True )
        
    def findByID (self , ID ):
        searchResult = None 
        if ( self.soLuongSinhVien() > 0 ) :
            for sv in self.listSinhVien :
                if sv.id == ID :
                    searchResult = sv
        return searchResult
    
    def findByName (self , keyWord ):
        listSV = []
        if ( self.soLuongSinhVien() > 0 ) :
              for sv in self.listSinhVien :
                if keyWord.lower() in sv.name.lower() :
                     listSV.append (sv)
        return listSV 
    
    def deleteByID (self , ID ):
        isDeleted = False
        sv = self.findByID (ID)
        if sv != None :
            self.listSinhVien.remove (sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc (self , sv : SinhVien ):
        if ( sv._diemTB >= 9 ) :
            sv._hocLuc = "Xuất sắc"
        elif ( sv._diemTB >= 8 ) :
            sv._hocLuc = "Giỏi"
        elif ( sv._diemTB >= 6.5 ) :
            sv._hocLuc = "Khá"
        elif ( sv._diemTB >= 5 ) :
            sv._hocLuc = "Trung bình"
        else :
            sv._hocLuc = "Yếu"
            
    def showSinhVien (self , listSV):
        print ("{:<8} {:<18} {:<8} {:<8} {:<8}" . format ("ID" , "Name" , "Sex" , "Major" , "DiemTB" , "Hoc Luc") )
        
        if ( listSV._len_ () > 0 ) :
            for sv in listSV :
                print ("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}" . format ( sv.id , sv.name , sv.sex , sv.major , sv.diemTB , sv._hocLuc ) )
        print ("\n")
        
        def getListSinhVien (self):
            return self.listSinhVien
        
        