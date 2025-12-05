class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # 1. Tạo các "rào" (rails)
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: xuống, -1: lên
        
        # 2. Xếp ký tự theo đường zigzag
        for char in plain_text:
            rails[rail_index].append(char)
            
            # Thay đổi hướng khi chạm đến rào trên cùng hoặc dưới cùng
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
                
            rail_index += direction
            
        # 3. Đọc các ký tự theo thứ tự từ trên xuống dưới
        cipher_text = "".join("".join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        text_length = len(cipher_text)
        rail_lengths = [0] * num_rails
        
        # 1. Tính toán độ dài của mỗi rào (tương tự bước zigzag)
        rail_index = 0
        direction = 1
        for _ in range(text_length):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        # 2. Chia bản mã thành các đoạn tương ứng với độ dài rào
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length
            
        # 3. Ghép các ký tự lại theo đường zigzag để giải mã
        plain_text = ""
        rail_index = 0
        direction = 1
        
        for _ in range(text_length):
            # Lấy ký tự đầu tiên từ rào hiện tại
            plain_text += rails[rail_index][0]
            # Xóa ký tự đã lấy khỏi rào
            rails[rail_index] = rails[rail_index][1:]
            
            # Thay đổi hướng
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text
