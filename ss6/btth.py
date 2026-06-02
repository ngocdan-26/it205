# PHẦN I - KHỞI TẠO HỆ THỐNG
kho_laptop = 0
kho_phone = 0
kho_tablet = 0

# PHẦN II - XÂY DỰNG MENU ĐIỀU HƯỚNG
while True:
    print("   HỆ THỐNG QUẢN LÝ KHO HÀNG")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")
    
    choice = input("Vui lòng chọn chức năng (1-5): ")
    
    # PHẦN V - XEM BÁO CÁO TỒN KHO (LỰA CHỌN 1)
    if choice == "1":
        print("\n--- BÁO CÁO TỒN KHO ---")
        print(f"Laptop hiện có: {kho_laptop} sản phẩm")
        print(f"Phone hiện có: {kho_phone} sản phẩm")
        print(f"Tablet hiện có: {kho_tablet} sản phẩm")
        
        # Yêu cầu nâng cao: Vẽ biểu đồ bằng dấu *
        print("\n--- BIỂU ĐỒ TRỰC QUAN ---")
        print(f"Laptop ({kho_laptop}): ", end="")
        for _ in range(kho_laptop):
            print("*", end="")
        print()
        
        print(f"Phone ({kho_phone}):  ", end="")
        for _ in range(kho_phone):
            print("*", end="")
        print()
        
        print(f"Tablet ({kho_tablet}): ", end="")
        for _ in range(kho_tablet):
            print("*", end="")
        print()

    # PHẦN III & IV - NHẬP KHO (LỰA CHỌN 2)
    elif choice == "2":
        print("\n--- NHẬP KHO HÀNG ---")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")
        loai_hang = int(input("Chọn mặt hàng muốn nhập (1-3): "))
        
        if loai_hang in range(1,4):
            # Vòng lặp kiểm tra dữ liệu âm (Phần IV - Validation)
            while True:
                so_luong_nhap = int(input("Nhập số lượng cần thêm: "))
                if so_luong_nhap >= 0:
                    break 
                else:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
            
            # Cộng dồn vào mặt hàng tương ứng
            if loai_hang == 1:
                kho_laptop += so_luong_nhap
                print(f"Đã nhập thành công {so_luong_nhap} Laptop.")
            elif loai_hang == 2:
                kho_phone += so_luong_nhap
                print(f"Đã nhập thành công {so_luong_nhap} Phone.")
            elif loai_hang == 3:
                kho_tablet += so_luong_nhap
                print(f"Đã nhập thành công {so_luong_nhap} Tablet.")
        else:
            print("Mặt hàng chọn không hợp lệ! Hủy thao tác nhập kho.")

    # PHẦN III & IV - XUẤT KHO (LỰA CHỌN 3)
    elif choice == "3":
        print("\n--- XUẤT KHO HÀNG ---")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")
        loai_hang = int(input("Chọn mặt hàng muốn xuất (1-3): "))
        
        if loai_hang in range(1,4):
            # Vòng lặp kiểm tra dữ liệu âm (Phần IV - Validation)
            while True:
                so_luong_xuat = int(input("Nhập số lượng cần xuất: "))
                if so_luong_xuat >= 0:
                    break
                else:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
            
            if loai_hang == 1:
                if so_luong_xuat <= kho_laptop:
                    kho_laptop -= so_luong_xuat
                    print(f"Đã xuất thành công {so_luong_xuat} Laptop.")
                else:
                    print("Không đủ hàng! Giao dịch xuất kho bị hủy.")
            elif loai_hang == 2:
                if so_luong_xuat <= kho_phone:
                    kho_phone -= so_luong_xuat
                    print(f"Đã xuất thành công {so_luong_xuat} Phone.")
                else:
                    print("Không đủ hàng! Giao dịch xuất kho bị hủy.")
            elif loai_hang == 3:
                if so_luong_xuat <= kho_tablet:
                    kho_tablet -= so_luong_xuat
                    print(f"Đã xuất thành công {so_luong_xuat} Tablet.")
                else:
                    print("Không đủ hàng! Giao dịch xuất kho bị hủy.")
        else:
            print("Mặt hàng chọn không hợp lệ! Hủy thao tác xuất kho.")

    # PHẦN V - CẢNH BÁO TỒN KHO THẤP (LỰA CHỌN 4)
    elif choice == "4":
        print("\n--- KIỂM TRA CẢNH BÁO TỒN KHO (< 10) ---")
        co_canh_bao = False
        
        if kho_laptop < 10:
            print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {kho_laptop} sản phẩm)")
            co_canh_bao = True
            
        if kho_phone < 10:
            print(f"[CẢNH BÁO] Mặt hàng Phone sắp hết (Chỉ còn {kho_phone} sản phẩm)")
            co_canh_bao = True
            
        if kho_tablet < 10:
            print(f"[CẢNH BÁO] Mặt hàng Tablet sắp hết (Chỉ còn {kho_tablet} sản phẩm)")
            co_canh_bao = True
            
        if not co_canh_bao:
            print("Tất cả các mặt hàng đều an toàn (Tồn kho >= 10).")

    # THOÁT CHƯƠNG TRÌNH (LỰA CHỌN 5)
    elif choice == "5":
        print("\nCảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
        break 

    # XỬ LÝ KHI NHẬP SAI MENU
    else:
        print("Lựa chọn không hợp lệ! Vui lòng nhập lại số từ 1 đến 5.")