class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        # Chuyển "J" thành "I" trong khóa
        key = key.replace("J", "I") 
        key = key.upper()
        key_set = set(key)
        # Bảng chữ cái Playfair 5x5 không dùng J
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
        
        # Lọc các ký tự còn lại từ bảng chữ cái không có trong khóa
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set]
            
        matrix = list(key)
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break
                
        # Chuyển danh sách 25 ký tự thành ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        # Xử lý trường hợp không tìm thấy
        return -1, -1 

    def playfair_encrypt(self, plain_text, matrix):
        # Chuẩn bị văn bản: loại bỏ khoảng trắng, chuyển J thành I, chuyển hoa
        plain_text = plain_text.replace(" ", "")
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""
        
        # Chia thành các cặp ký tự và xử lý ký tự trùng lặp/lẻ
        i = 0
        while i < len(plain_text):
            pair = plain_text[i:i+2]
            
            if len(pair) == 1: # Xử lý nếu số lượng ký tự lẻ
                pair += "X"
                i += 1
            elif pair[0] == pair[1]: # Xử lý nếu hai ký tự trùng lặp
                pair = pair[0] + "X"
                i += 1
            else:
                i += 2
                
            # Mã hóa cặp ký tự
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2: # Cùng hàng: dịch phải 1 vị trí (mod 5)
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2: # Cùng cột: dịch xuống 1 vị trí (mod 5)
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else: # Tạo hình chữ nhật: lấy ký tự ở góc chéo còn lại
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        # 1. Giải mã theo quy tắc Playfair tiêu chuẩn
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2: # Cùng hàng: dịch trái 1 vị trí (ngược lại mã hóa)
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2: # Cùng cột: dịch lên 1 vị trí (ngược lại mã hóa)
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else: # Tạo hình chữ nhật: lấy ký tự ở góc chéo còn lại (giống mã hóa)
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        # [cite_start]2. HẬU XỬ LÝ (POST-PROCESSING) - Logic banro từ tài liệu [cite: 977-1002]
        # Xử lý để loại bỏ ký tự đệm 'X' và khôi phục ký tự trùng lặp
        banro = ""
        
        # Lặp qua các cặp (bước nhảy 2) để kiểm tra ký tự đệm/trùng lặp
        for i in range(0, len(decrypted_text)-2, 2): 
            if decrypted_text[i] == decrypted_text[i+2]:
                # Trường hợp ký tự trùng lặp (ví dụ: L X L -> L)
                banro += decrypted_text[i]
            else:
                # Trường hợp ký tự bình thường
                banro += decrypted_text[i] + "" + decrypted_text[i+1]
        
        # Xử lý hai ký tự cuối cùng của chuỗi đã giải mã
        # Kiểm tra nếu ký tự cuối cùng là 'X' đệm (padding)
        if decrypted_text[-1] == "X": 
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2]
            banro += decrypted_text[-1]
            
        return banro