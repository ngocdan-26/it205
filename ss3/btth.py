while True:
    so_luong = int(input("Nhập số lượng nhân viên: "))

    for i in range(1, so_luong + 1):
        print(f"\nNhân viên {i}")
        
        ten = input("Tên nhân viên: ")
        so_ngay_lam = int(input("Số ngày đi làm: "))

        print("Thông tin nhân viên:")
        print(f"Tên: {ten}")
        print(f"Số ngày đi làm: {so_ngay_lam}")

        if so_ngay_lam < 20:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")
    print("\n-----------------------------------------")
    lua_chon = input("Tiếp tục chương trình? (y/n): ")
    if lua_chon == 'n':
        print("Chương trình kết thúc.")
        break  