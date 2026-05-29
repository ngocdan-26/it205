number = 200
value = 0
while value < 5:
    value += 1
    is_number = int(input(f"Lượt đoán {value} - Nhập số của bạn: "))
    if is_number < number:
        print("=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")
    elif is_number > number:
        print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")
    else :
        print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        break
print("--- TRÒ CHƠI KẾT THÚC ---")
