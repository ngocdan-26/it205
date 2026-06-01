num_employees = int(input("nhập số lượng nhân viên cần kiểm tra: "))
for i in range(num_employees):
    employees = input("Nhập tên nhân viên: ")
    num_days = int(input("Nhập số ngày làm việc trong tháng(0 → 22): "))
    if num_days < 0 or num_days > 22:
        print("Dữ liệu không hợp lệ!")
        continue
    elif num_days == 0 :
        print("nhân viên nghỉ toàn bộ tháng ") 
    else:
        print(f"{employees}: ",end="")
        for j in range(num_days):
            print("*",end="")
        print()
        if num_days >= 18:
            print("Làm việc chăm chỉ")
        elif num_days < 10:
            print("Làm việc ít")
        else:
            print("Làm việc bình thường")