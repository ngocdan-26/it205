class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available

menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

while True:
    print("""
        === HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===
        1. Xem danh sách đồ uống
        2. Thêm đồ uống mới
        3. Cập nhật trạng thái kinh doanh
        4. Thoát chương trình
        ===============================================
""")

    choice = input("Chọn chức năng (1-4): ")
    if choice == "1":
        print("\n--- DANH SÁCH ĐỒ UỐNG ---")
        print("Mã món | Tên món | Giá bán | Trạng thái")
        print("-" * 50)
        for drink in menu:
            status = "Đang bán" if drink.is_available else "Ngừng bán"
            print(f"{drink.code} | {drink.name} | {drink.price} | {status}")

    elif choice == "2":
        code = input("Nhập mã món: ").strip()
        is_exist = False
        for drink in menu:
            if drink.code == code:
                is_exist = True
                break
        if is_exist:
            print("Mã món đã tồn tại trong hệ thống!")
            continue
        name = input("Nhập tên món: ").strip()
        try:
            price = int(input("Nhập giá bán: "))
            if price <= 0:
                print("Giá bán không hợp lệ!")
                continue
            new_drink = Drink(code, name, price)
            menu.append(new_drink)
            print(f"Thành công: Đã thêm món {name} vào thực đơn!")
        except ValueError:
            print("Giá bán không hợp lệ!")

    elif choice == "3":
        code = input("Nhập mã món cần cập nhật: ").strip()
        found = False
        for drink in menu:
            if drink.code == code:
                drink.toggle_available()
                status = ("Đang bán" if drink.is_available else "Ngừng bán")
                print(f"Đã cập nhật trạng thái món {code}.")
                print(f"Trạng thái hiện tại: {status}")
                found = True
                break
        if not found:
            print("Không tìm thấy món có mã này!")

    elif choice == "4":
        print("Cảm ơn bạn đã sử dụng hệ thống")
        break

    else:
        print("Lựa chọn không hợp lệ!")
