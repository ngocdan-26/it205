product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]
while True :
    print("""  ===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
                1. Hiển thị danh sách sản phẩm
                2. Thêm sản phẩm mới
                3. Cập nhật thông tin sản phẩm
                4. Xóa sản phẩm theo mã
                5. Thoát chương trình""")
    choice = input("Mời bạn chọn chức năng (1-5): ")
    if choice == "1":
        if not product_list:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            for index, prod in enumerate(product_list, start=1):
                    print(f"{index}. Mã SP: {prod['product_id']} | Tên: {prod['product_name']} | Giá: {prod['price']} | Số lượng: {prod['quantity']}")
    elif choice =="2":
        prod_id = input("Nhập mã sản phẩm: ").strip().upper()
        if not prod_id:
            print("Mã sản phẩm không được để trống!")
            continue
        duplicate = False
        for prod in product_list:
            if prod["product_id"] == prod_id:
                 duplicate = True
                 break
        if duplicate == True:
             print("Mã sản phẩm bị trùng!")
             continue
        
        prod_name = input("Nhập tên sản phẩm: ").strip()
        price_str = input("Nhập giá sản phẩm: ").strip()
        quantity_str = input("Nhập số lượng sản phẩm: ").strip()

        if not price_str.isdigit() or not quantity_str.isdigit():
            print("Giá/Số lượng không hợp lệ!")
            continue

        price = int(price_str)
        quantity = int(quantity_str)

        if price <= 0 or quantity <= 0:
            print("Giá/Số lượng không hợp lệ!")
            continue

        new_product = {
            "product_id": prod_id,
            "product_name": prod_name,
            "price": price,
            "quantity": quantity
        }
        product_list.append(new_product)
        print("Thêm sản phẩm thành công!")

    elif choice == "3":
        prod_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

        found_product = None

        for prod in product_list:
            if prod["product_id"] == prod_id:
                found_product = prod
                break

        if found_product is None:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
        else:
            new_name = input("Nhập tên sản phẩm mới: ").strip()
            new_price_raw = input("Nhập giá sản phẩm mới: ").strip()
            new_quantity_raw = input("Nhập số lượng tồn kho mới: ").strip()
            
            if not (new_price_raw.isdigit() and new_quantity_raw.isdigit()):
                print("Giá/Số lượng không hợp lệ")
            else:
                new_price = int(new_price_raw)
                new_quantity = int(new_quantity_raw)
                
                if new_price <= 0 or new_quantity <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    found_product["product_name"] = new_name
                    found_product["price"] = new_price
                    found_product["quantity"] = new_quantity
                    print("Cập nhật thông tin sản phẩm thành công!")
        
    elif choice == "4":
        product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        
        found_product = None
        for prod in product_list:
            if prod["product_id"] == product_id:
                found_product = prod
                break
                
        if found_product is None:
            print("Không tìm thấy mã sản phẩm cần xoá!")
        else:
            product_list.remove(found_product)
            print("Xóa sản phẩm thành công!")

    elif choice == "5":
        print("Thoát chương trình.")
        break
        
    else:
        print('"Lựa chọn không hợp lệ", vui lòng nhập lại!')       