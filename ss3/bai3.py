for employee_number in range(1, 4):
    print(f"--- Nhập thông tin nhân viên số {employee_number} ---")
    # Input mã nhân viên, họ và tên, phòng ban
    employee_id = input("Nhập mã nhân viên: ")
    employee_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")

    # Kiểm tra dữ liệu không hợp lệ
    if employee_id.strip() == "" or employee_name.strip() == "":
        print("\n[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ!")
        print("Hủy bỏ tạo hồ sơ cho nhân viên này.")
        print("----------------------------------------\n")
        continue

print(" --- HỒ SƠ NHÂN SỰ ĐIỆN TỬ ---")
for employee_number in range(1, 4):
    # Output mã nhân viên, họ và tên, phòng ban
    print(f"Mã nhân viên : {employee_id}")
    print(f"Họ và tên    : {employee_name}")
    print(f"Phòng ban    : {department}")

print("Đã hoàn tất khởi tạo hồ sơ cho 3 nhân viên!")