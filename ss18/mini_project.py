products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def show_products(products_list):
    if not products_list:
        print("Cửa hàng hiện chưa có sản phẩm nào!")
    else:
        print("--- Danh sách sản phẩm ---")
        print("ID    | Tên sản phẩm  |  Giá bán ")
        print("-------------------------------------")
        for pro in products_list:
            print(f"{pro["id"]}   | {pro["name"]}  | {pro["price"]}")
            print("-------------------------------------")

def add_product(products_list):
    while True:
        pro_id = input("Nhập id sản phẩm: ").strip().upper()
        check = True
        for pro in products_list:
            if pro["id"] == pro_id:
                check = False
                break
        if not pro_id :
            print("ID không được để trống!")
            check = False
        if check == False:
            print("ID không được trùng")
            continue
        else:
            break
        
        
    while True:
        pro_name = input("Nhập tên sản phẩm: ").strip().lower().title()
        if not pro_name:
            print("Tên không được để trống!")
            continue
        else:
            break
    while True:
        pro_price = input("Nhập giá bán: ").strip()
        if pro_price.isdigit():
            price = int(pro_price)
            if price > 0:
                break
            else:
                print("giá phải lớn hơn 0!")
                continue
        else:
            print("giá không hợp lệ")
            continue
    new_product = {
        "id" : pro_id,
        "name" : pro_name,
        "price" : price
    }
    products_list.append(new_product)

def update_price(products_list):
    check_id = input("Nhập mã sản phẩm cần sửa giá: ").strip().upper()
    print("--- Cập nhật giá sản phẩm ---")
    for pro in products_list:
        if check_id == pro["id"]:
            print(f"Tìm thấy sản phẩm: {pro["name"]} (Giá hiện tại: {pro["price"]})")
            while True:
                new_price = input("Nhập giá mới: ")
                if new_price.isdigit():
                    price = int(new_price)
                    if price > 0:
                        pro["price"] = price
                        print("cap nhat thanh cong")
                        break
                    else:
                        print("giá phải lớn hơn 0!")
                        continue
                else:
                    print("giá không hợp lệ")
                    continue
    print(f"khong tim thaysp co ma [{check_id}]")

while True:
    print("""
        =====================================
            Quản lý cửa hàng - Mini store
        =====================================
        1. xem danh sách sp hiện có 
        2. Thêm mới một sản phẩm 
        3. Cập nhật giá sản phẩm theo ID
        4. Thoát chương trình 
        =====================================
""")
    
    choice = input("chọn chức năng của bạn(1-4): ")
    if choice == "1":
        show_products(products)
    elif choice == "2":
        add_product(products)
    elif choice == "3":
        update_price(products)
    elif choice == "4":
        print("Bạn đã thoát khỏi chương trình")
        break
