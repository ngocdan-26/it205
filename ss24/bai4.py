import re


class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.title()
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if value > 0:
            self.__base_price = value
        else:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return int(
            self.__base_price +
            self.__base_price * MenuItem.service_charge
        )

    @classmethod
    def update_service_charge(cls, new_rate):
        if new_rate >= 0:
            cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_code):
        pattern = r"^[A-Z]{2}\d{2}$"
        return bool(re.match(pattern, item_code))


menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]


while True:
    print("""
===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====
1. Xem thực đơn & Giá niêm yết
2. Thêm món mới vào menu
3. Cập nhật trạng thái (Hết hàng/Còn hàng)
4. Điều chỉnh giá gốc của món
5. Cập nhật phụ phí dịch vụ toàn hệ thống
6. Thoát chương trình
======================================================
""")

    choice = input("Chọn chức năng (1-6): ")
    if choice == "1":
        print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")
        for i, item in enumerate(menu_db, start=1):
            status = ("Đang bán" if item.is_available else "Hết hàng")
            print(
                f"{i}. Mã: {item.item_id} | "
                f"Tên: {item.item_name} | "
                f"Trạng thái: {status} | "
                f"Giá niêm yết: "
                f"{item.calculate_selling_price():,} VNĐ"
            )

    elif choice == "2":
        print("\n--- THÊM MÓN MỚI VÀO MENU ---")
        item_id = input("Nhập mã món: ").strip()
        exist = False
        for item in menu_db:
            if item.item_id == item_id:
                exist = True
                break
        if exist:
            print("Mã món đã tồn tại!")
            continue
        if not MenuItem.is_valid_item_id(item_id):
            print("Mã món không hợp lệ!")
            print("Mã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01.")
            continue
        item_name = input("Nhập tên món: ")
        try:
            base_price = int(input("Nhập giá gốc: "))
            if base_price <= 0:
                print("Giá đồ uống phải lớn hơn 0!")
                continue
            menu_db.append(MenuItem(item_id, item_name, base_price))
            print("Thêm món mới thành công!")
        except ValueError:
            print("Giá không hợp lệ!")

    elif choice == "3":
        print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")
        item_id = input("Nhập mã món cần cập nhật: ")
        found = None
        for item in menu_db:
            if item.item_id == item_id:
                found = item
                break
        if found:
            found.toggle_availability()
            status = ("ĐANG BÁN" if found.is_available else "HẾT HÀNG")
            print(f">> Đã cập nhật {found.item_name} thành {status}!")
        else:
            print("Không tìm thấy món!")

    elif choice == "4":
        print( "\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
        item_id = input( "Nhập mã món cần đổi giá: ")
        found = None
        for item in menu_db:
            if item.item_id == item_id:
                found = item
                break
        if found:
            try:
                new_price = int(input("Nhập giá tiền mới: "))
                old_price = found.base_price
                found.base_price = new_price
                if (new_price > 0 and found.base_price != old_price):
                    print("Cập nhật giá gốc thành công!")
            except ValueError:
                print("Giá không hợp lệ!")
        else:
            print("Không tìm thấy món!")

    elif choice == "5":
        print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
        print(f"Phụ phí hiện tại: {MenuItem.service_charge * 100:.0f}%")

        try:
            new_rate = float(input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: "))
            if new_rate < 0:
                print("Phụ phí không hợp lệ!")
                continue
            MenuItem.update_service_charge(new_rate)
            print("Cập nhật phụ phí dịch vụ thành công!")
        except ValueError:
            print("Dữ liệu không hợp lệ!")
    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ!")