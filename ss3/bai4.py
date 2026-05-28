# CÁCH 1: SỬ DỤNG while True
# Ý tưởng:
# - Cho vòng lặp chạy vô hạn
# - Nếu nhập hợp lệ (>0) thì dùng break để thoát

while True:
    so_luong_nhan_su = int(input("nhập số lượng nhân sự: "))
    if so_luong_nhan_su > 0:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu ")
        print(f"cấp phát tài sản cho {so_luong_nhan_su} nhân sự mới!")
        break
    else:
        print("[LỖI] Số lượng không hợp lệ! ")
print("CHƯƠNG TRÌNH KẾT THÚC")

# CÁCH 2: SỬ DỤNG while điều kiện
# Ý tưởng:
# - Khởi tạo giá trị sai trước (=0)
# - Chừng nào số lượng <=0 thì bắt nhập lại

so_luong_nhan_su = 0
while so_luong_nhan_su <= 0:

    so_luong_nhan_su = int(input("nhập số lượng nhân sự: "))
    if so_luong_nhan_su <= 0:
        print("[LỖI] Số lượng không hợp lệ! ")

print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu ")
print(f"cấp phát tài sản cho {so_luong_nhan_su} nhân sự mới!")

print("CHƯƠNG TRÌNH KẾT THÚC")

# | Tiêu chí              | `while True` | `while điều kiện` |
# | --------------------- | ------------ | ----------------- |
# | Độ ngắn gọn của code  |  Ngắn hơn    |  Dài hơn chút     |
# | Dễ hiểu với người đọc |  Trung bình  |  Dễ hiểu hơn      |
# | Gần ngôn ngữ tự nhiên |  Không gần   |  Gần              |
# | Dễ mở rộng logic      |  Dễ          |  Trung bình       |

# -> chọn cách 2
