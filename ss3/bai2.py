print(" --- HỆ THỐNG GỬI EMAIL THƯỜNG TẾT --- ")
# Vòng lặp chạy dúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")
    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input("Nhập số ngày công trong tháng: "))
# Kiểm tra diều kiện
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghi cả tháng. Không xét duyệt thưởng.")
        continue
    bonus_amount = working_days * 200000
    print("-> Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VNĐ tiên thưởng!")
    print("------------------------------------\n")
print("Đã hoàn tất quá trình duyệt thường cho 3 nhân viên!")