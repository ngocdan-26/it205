saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]
while True:
    print("""
            ===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
            1. Xem danh sách sổ tiết kiệm
            2. Mở sổ tiết kiệm mới
            3. Cập nhật thông tin sổ tiết kiệm
            4. Tất toán hoặc xóa sổ tiết kiệm
            5. Tính lãi dự kiến khi đến hạn
            6. Kiểm tra điều kiện rút trước hạn
            7. Thoát chương trình
    """)
    choice = input("Mời bạn chọn chức năng (1-7): ")
    if choice == "1":
        if not saving_accounts:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sổ tiết kiệm:")
            for i, acc in enumerate(saving_accounts ,start = 1):
                print(f"{i}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']}| Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
    
    elif choice == "2":
        acc_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        duplicate = False
        for acc in saving_accounts:
            if acc["account_id"] == acc_id:
                 duplicate = True
                 break
        if duplicate == True:
             print("Mã sổ tiết kiệm đã tồn tại!")
             continue
        
        acc_name = input("Nhập tên khách hàng: ").strip()
        if not acc_name:
            print("Tên khách hàng không được để trống.")
            continue

        acc_balance = input("Nhập số tiền gửi: ").strip()
        if not acc_balance.isdigit() :
            print("Số tiền gửi phải là số nguyên dương.")
            continue

        acc_term_months = input("Nhập kỳ hạn gửi theo tháng: ")
        if not acc_term_months.isdigit():
            print("Kỳ hạn gửi phải là số nguyên dương.")
            continue

        try:
            interest_rate = float(input("Nhập lãi suất năm: "))
            if interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue
        except ValueError:
            print("Lãi suất không hợp lệ!")
            continue
        new_account = {
            "account_id": acc_id,
            "customer_name": acc_name,
            "balance": int(acc_balance),
            "term_months": int(acc_term_months),
            "interest_rate": interest_rate,
            "status": "active"
        }
        saving_accounts.append(new_account)
    
    elif choice == "3":
        acc_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()

        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == acc_id:
                found_account = acc
                break

        if found_account is None:
            print("Không tìm thấy mã sổ tiết kiệm.")
            continue

        if found_account["status"] == "closed":
            print("Không thể cập nhật sổ tiết kiệm đã tất toán.")
            continue

        new_name = input("Nhập tên khách hàng mới: ").strip()
        if not new_name:
            print("Tên khách hàng không được để trống.")
            continue

        new_balance = input("Nhập số tiền gửi mới: ").strip()
        if not new_balance.isdigit():
            print("Số tiền gửi phải là số nguyên dương.")
            continue

        new_term = input("Nhập kỳ hạn mới theo tháng: ").strip()
        if not new_term.isdigit():
            print("Kỳ hạn gửi phải là số nguyên dương.")
            continue

        try:
            new_rate = float(input("Nhập lãi suất năm mới: "))
            if new_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue
        except ValueError:
            print("Lãi suất không hợp lệ!")
            continue

        found_account["customer_name"] = new_name
        found_account["balance"] = int(new_balance)
        found_account["term_months"] = int(new_term)
        found_account["interest_rate"] = new_rate

    elif choice == "4":
        acc_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == acc_id:
                found_account = acc
                break

        if found_account is None:
            print("Không tìm thấy mã sổ tiết kiệm.")
            continue

        if found_account["status"] == "closed":
            print("Sổ tiết kiệm đã được tất toán trước đó.")
            continue

        found_account["status"] = "closed"

        print(f"Tất toán sổ tiết kiệm {acc_id} thành công!")
    elif choice == "5":
        acc_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()

        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == acc_id:
                found_account = acc
                break

        if found_account is None:
            print("Không tìm thấy mã sổ tiết kiệm.")
            continue

        if found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán.")
            continue

        interest = ( found_account["balance"]
            * found_account["interest_rate"]/ 100
            * found_account["term_months"] / 12)

        total_received = found_account["balance"] + interest

        print(f"\n--- KẾT QUẢ TÍNH LÃI DỰ KIẾN (MÃ SỔ: {acc_id}) ---")
        print(f"Số tiền gốc: {found_account['balance']:,} VND")
        print(f"Tiền lãi dự kiến nhận được: {interest:,.0f} VND")
        print(f"Tổng tiền nhận khi đến hạn: {total_received:,.0f} VND")
    
    elif choice == "6":
        acc_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()

        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == acc_id:
                found_account = acc
                break

        if found_account is None:
            print("Không tìm thấy mã sổ tiết kiệm.")
            continue

        if found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán.")
            continue

        actual_months = input("Nhập số tháng thực gửi: ").strip()

        if not actual_months.isdigit() or int(actual_months) <= 0:
            print("Số tháng thực gửi không hợp lệ!")
            continue

        actual_months = int(actual_months)

        if actual_months < found_account["term_months"]:
            applied_rate = 0.5
            print("Khách hàng rút TRƯỚC HẠN.")
            print("Áp dụng lãi suất không kỳ hạn: 0.5%/năm.")
        else:
            applied_rate = found_account["interest_rate"]
            print("Khách hàng rút ĐÚNG/SAU HẠN.")
            print("Áp dụng lãi suất ban đầu.")

        actual_interest = ( found_account["balance"] * applied_rate / 100 * actual_months / 12)

        total_actual_received = found_account["balance"] + actual_interest

        print(f"\n--- KẾT QUẢ RÚT TIỀN THỰC TẾ (MÃ SỔ: {acc_id}) ---")
        print(f"Số tiền gốc: {found_account['balance']:,} VND")
        print(f"Số tháng thực gửi: {actual_months} tháng")
        print(f"Lãi suất áp dụng: {applied_rate}%/năm")
        print(f"Tiền lãi thực nhận: {actual_interest:,.0f} VND")
        print(f"Tổng tiền thực nhận: {total_actual_received:,.0f} VND")

    elif choice == "7":
        print("Cảm ơn bạn đã sử dụng hệ thống quản lý TechBank")
        break
    
    else:
        print("dữ liệu nhập không hợp lệ")