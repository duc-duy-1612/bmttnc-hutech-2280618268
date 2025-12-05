class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                # Tính toán độ dịch chuyển (shift) từ ký tự khóa (key)
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                
                if char.isupper():
                    # Mã hóa chữ hoa: E(x) = (x + k) mod 26
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    # Mã hóa chữ thường: E(x) = (x + k) mod 26
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                
                key_index += 1 # Chuyển sang ký tự khóa tiếp theo
            else:
                encrypted_text += char # Giữ nguyên ký tự không phải chữ cái
                
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                # Tính toán độ dịch chuyển (shift) từ ký tự khóa (key)
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                
                if char.isupper():
                    # Giải mã chữ hoa: D(x) = (x - k) mod 26
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    # Giải mã chữ thường: D(x) = (x - k) mod 26
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                
                key_index += 1 # Chuyển sang ký tự khóa tiếp theo
            else:
                decrypted_text += char # Giữ nguyên ký tự không phải chữ cái
                
        return decrypted_text