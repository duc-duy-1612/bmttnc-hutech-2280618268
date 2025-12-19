import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                # Trích xuất bit cuối cùng của mỗi kênh màu
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""
    for i in range(0, len(binary_message), 8):
        # Chuyển đổi mỗi 8 bit thành một ký tự
        char = chr(int(binary_message[i:i+8], 2))
        
        # Kiểm tra dấu hiệu kết thúc (ở đây code mẫu dùng '\0' hoặc nhận diện chuỗi kết thúc)
        # Lưu ý: Code mẫu của bạn kiểm tra ký tự '\0'
        if char == '\0': 
            break
        # Hoặc kiểm tra chuỗi kết thúc đặc biệt 16-bit nếu cần chính xác như lúc mã hóa
        if binary_message[i:i+16] == '1111111111111110':
            break
            
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()