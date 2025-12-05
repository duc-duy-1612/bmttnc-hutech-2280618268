from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher # Import logic đã tạo ở Bài 1

app = Flask(__name__)

# Khởi tạo Caesar Cipher
Caesar = CaesarCipher()

# Route cho trang chủ
@app.route("/")
def home():
    return render_template('index.html')

# Route cho giao diện Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route xử lý Mã hóa (POST từ form)
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    # Thực hiện mã hóa
    encrypted_text = Caesar.encrypt_text(text, key)
    
    # Trả về kết quả thô
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Route xử lý Giải mã (POST từ form)
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    # Thực hiện giải mã
    decrypted_text = Caesar.decrypt_text(text, key)
    
    # Trả về kết quả thô
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# main function
if __name__ == "__main__":
    # Chạy trên cổng 5050 để tránh xung đột với API (cổng 5000)
    app.run(host="0.0.0.0", port=5050, debug=True) 
