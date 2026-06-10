saff_manager = []

while True:
    print("""
            --- Quản lý nhân sự - saff manager ---
          1. Thêm nhân viên mới
          2. Danh sách nhân viên
          3. Xóa nhân viên khỏi hệ thống
          4. thoát chương trình
""")
    choice = input("Mời bạn chọn chức năng (1-4): ")

    if choice == "1":
        saff_id = 101
        for saff in saff_manager:
            if saff_id == saff["id"]:
                saff_id += 1
        saff_name = input("Nhập tên nhân viên: ").strip().lower().title()
        if not saff_name:
            print("Tên nhân viên không được để trống")
            continue
        while True:
            salary = float(input("Nhập mức lương: "))
            
            if salary < 0:
                print("Mức lương kh đúng yêu cầu. Mời nhập lại!")
                continue
            break
        new_saff = {
            "id" : saff_id,
            "name" : saff_name,
            "salary" : salary
        }
        saff_manager.append(new_saff)
        print(f"Thêm nhân viên thành công! ID: {saff_id}")

    elif choice == "2":
        if not saff_manager:
            print("Chưa có dữ liệu nhân sự!")
            continue
        print("ID   |  Tên nhân viên  | Mức Lương")
        for i , saff in enumerate(saff_manager , start=1):
            print(f"{saff["id"]}  |  {saff["name"]}  |  {saff["salary"]}")
    elif choice == "3":
        seach = input("Nhập ID: ").strip()
        is_seach = False
        if not seach.isdigit():
            print("Không tìm thấy nhân viên để xóa!")
            continue
        
        saff_id = int(seach)

        for saff in saff_manager:
            if saff_id == saff["id"]:
                saff_manager.remove(saff) 
                is_seach = True
                print(f"Đã xóa nhân viên ID {saff_id} thành công!")
        if not is_seach:
            print("Không tìm thấy nhân viên để xóa!")
    elif choice == "4":
        print("Bạn đã thoát khỏi chương trình")    
        break
    else:
        print("lựa chọn không hợp lệ mời nhập lại")