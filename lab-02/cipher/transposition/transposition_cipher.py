class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        """ Mã hóa (giữ nguyên theo tài liệu). """
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        """
        Giải mã: Xây dựng lại các cột (columns) và đọc theo hàng (rows).
        Sử dụng logic tính toán độ dài cột.
        """
        text_length = len(text)
        # Số hàng (rows). Ví dụ: 10 ký tự, key=3 -> 4 hàng
        num_rows = (text_length + key - 1) // key
        
        # Số ô bị thiếu (shaded boxes) ở hàng cuối
        num_shaded_boxes = (num_rows * key) - text_length
        
        # Tạo danh sách rỗng để lưu trữ các đoạn cột
        decrypted_text_columns = [''] * key
        
        # Chiếu bản mã vào các cột theo độ dài chính xác của chúng
        text_index = 0
        for col in range(key):
            # Chiều cao của cột: num_rows nếu không bị thiếu, num_rows - 1 nếu bị thiếu
            col_len = num_rows
            
            # Cột bị thiếu là những cột ở cuối, số lượng bằng num_shaded_boxes
            # Nếu chỉ số cột hiện tại (col) lớn hơn hoặc bằng (key - num_shaded_boxes) thì cột đó ngắn hơn
            if col >= key - num_shaded_boxes:
                col_len -= 1

            # Lấy các ký tự cho cột hiện tại từ bản mã
            column_segment = text[text_index:text_index + col_len]
            decrypted_text_columns[col] = column_segment
            text_index += col_len

        # Đọc các ký tự theo hàng ngang để khôi phục bản rõ
        plain_text = ""
        for row in range(num_rows):
            for col in range(key):
                # Đảm bảo không truy cập index ngoài phạm vi cột
                if row < len(decrypted_text_columns[col]):
                    plain_text += decrypted_text_columns[col][row]
                    
        return plain_text