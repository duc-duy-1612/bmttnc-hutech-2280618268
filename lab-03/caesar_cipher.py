import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # SỬA: Đảm bảo tên nút Decrypt là 'btn_descrypt' theo UI của bạn
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt) 
        self.ui.btn_descrypt.clicked.connect(self.call_api_decrypt) 

    def get_key_value(self):
        """Hàm lấy giá trị Key và kiểm tra tính hợp lệ."""
        key_str = self.ui.textEdit_2.toPlainText().strip()
        if not key_str:
            QMessageBox.warning(self, "Lỗi Nhập Liệu", "Vui lòng nhập giá trị Key (phải là số nguyên).")
            return None
        try:
            # Kiểm tra xem có thể chuyển thành số nguyên không
            key = int(key_str) 
            return key_str # Trả về chuỗi Key đã được kiểm tra để gửi qua JSON
        except ValueError:
            QMessageBox.critical(self, "Lỗi Key", "Key phải là một số nguyên.")
            return None
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt" 
        key_value = self.get_key_value()
        if key_value is None:
            return # Dừng nếu Key không hợp lệ
            
        payload = {
            "plain_text": self.ui.textEdit.toPlainText(), 
            "key": key_value 
        }
        try:
            response = requests.post(url, json=payload) 

            if response.status_code == 200: 
                data = response.json() 
                self.ui.textEdit_3.setText(data["encrypted_message"]) 
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information) 
                msg.setText("Encrypted Successfully")
                msg.exec_() 
            else:
                # Nếu server trả về lỗi 400 hoặc 500
                QMessageBox.critical(self, "Lỗi API", f"Mã hóa thất bại. Mã trạng thái: {response.status_code}")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi Kết Nối", f"Không thể kết nối đến API. Vui lòng kiểm tra API server đã chạy chưa.\nChi tiết lỗi: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt" 
        key_value = self.get_key_value()
        if key_value is None:
            return # Dừng nếu Key không hợp lệ

        payload = {
            "cipher_text": self.ui.textEdit_3.toPlainText(), 
            "key": key_value
        }

        try:
            response = requests.post(url, json=payload) 

            if response.status_code == 200: 
                data = response.json() 
                self.ui.textEdit.setText(data["decrypted_message"])
                msg = QMessageBox() 
                msg.setIcon(QMessageBox.Information) 
                msg.setText("Decrypted Successfully") 
                msg.exec_() 
            else:
                # Nếu server trả về lỗi 400 hoặc 500
                QMessageBox.critical(self, "Lỗi API", f"Giải mã thất bại. Mã trạng thái: {response.status_code}")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi Kết Nối", f"Không thể kết nối đến API. Vui lòng kiểm tra API server đã chạy chưa.\nChi tiết lỗi: {e}")

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MyApp() 
    window.show() 
    sys.exit(app.exec_())