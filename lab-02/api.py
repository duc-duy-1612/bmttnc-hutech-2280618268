from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher # <== THÊM IMPORT BÀI 3

app = Flask(__name__)

# KHỞI TẠO CÁC ALGORITHM
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher() # <== KHỞI TẠO BÀI 3

# ==================================
# CAESAR CIPHER ENDPOINTS
# ==================================

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    """ Mã hóa bản rõ bằng Caesar Cipher. """
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    """ Giải mã bản mã bằng Caesar Cipher. """
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# ==================================
# VIGENERE CIPHER ENDPOINTS
# ==================================

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    """ Mã hóa bản rõ bằng Vigenère Cipher. """
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    """ Giải mã bản mã bằng Vigenère Cipher. """
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ==================================
# RAIL FENCE CIPHER ENDPOINTS <== THÊM ĐOẠN CODE NÀY
# ==================================

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    """ Mã hóa bản rõ bằng Rail Fence Cipher. """
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    """ Giải mã bản mã bằng Rail Fence Cipher. """
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)