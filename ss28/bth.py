
class Product:
    def __init__(self, product_id, name, price,quantity_sold, discount):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.total_revenue = 0
        self.revenue_type = ""
        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        revenue = self.price * self.quantity_sold - self.discount
        self.total_revenue = max(0, revenue)

    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"  
    
class ProductManager:
    def __init__(self):
        self.products = []
    
    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def add_product(self):
        product_id = input("nhập mã SP: ").strip().upper()
        if product_id == "":
            print("Id không được để trống")
            return
        if self.find_by_id(product_id):
            print("Mã sản phẩm đã tồn tại")
            return
        name = input("Tên sản phẩm: ").strip().lower().title()
        if name == "":
            print("Tên sản phẩm không được để trống!")
            return
        try:
            price = float(input("Giá bán: "))
            quantity_sold = int(input("Số lượng đã bán: "))
            discount = float(input("Giảm giá: "))
        except ValueError:
            print("Dữ liệu không hợp lệ!")
            return
        if price < 0:
            print("Giá bán phải >= 0!")
            return
        if quantity_sold < 0 or quantity_sold > 10000:
            print("Số lượng phải từ 0 đến 10000!")
            return
        if discount < 0:
            print("Giảm giá phải >= 0!")
            return
        product = Product(
            product_id, name, price, quantity_sold, discount)
        self.products.append(product)
        print("Thêm sản phẩm thành công!")

    def show_all(self):
        if len(self.products) == 0:
            print("Danh sách sản phẩm đang rỗng!")
            return
        print("Danh sách sản phẩm")
        print(f"{"Mã SP":<10} | {"Tên SP":<20} | {"Giá":<12} | {"SL Bán":<10} | {"Giảm giá":<12} | {"Doanh thu":<15} | {"Loại":<10}")
        for product in self.products:
            print(f"{product.id:<10} | {product.name:<20} | {product.price:<12} | {product.quantity_sold:<10} | {product.discount:<12.0f} | {product.total_revenue:<15.0f} | {product.revenue_type:<10}")

    def update_product(self):
        product_id = input("Nhập id cần sửa: ").strip().upper()
        product = self.find_by_id(product_id)
        if not product:
            print("Không tìm thấy sản phẩm cần cập nhật")
            return
        
        try:
            product.price = float(input("Giá mới: "))
            product.quantity_sold = int(input("SL bán mới: "))
            product.discount = float(input("Giảm giá mới: "))
        except ValueError:
            print("Dữ liệu không hợp lệ!")
            return
        
        product.calculate_revenue()
        product.classify_revenue()
        print("Cập nhật sản phẩm thành công!")

    def delete_product(self):
        product_id = input("Nhập id cần xóa: ").strip().upper()
        product = self.find_by_id(product_id)
        if not product:
            print("Không tìm thấy sản phẩm cần xóa")
            return
        confirm = input("Bạn có chắc muốn xóa sản phẩm này không? (Y/N): ").lower().strip()
        if confirm == "y":
            self.products.remove(product)
            print("Xóa sản phẩm thành công!")
        elif confirm == "n":
            print("Đã hủy thao tác xóa")
        else:
            print("Lụa chọn không hợp lệ")
        
    def search_product(self):
        search_name = input("Nhập tên cần tìm kiếm: ").lower()
        result = []
        for product in self.products:
            if search_name in product.name:
                result.append(product)
        if len(result) == 0:
            print("Không tìm thấy sản phẩm phù hợp!")
            return
        for product in result:
            print(f"{product.id} - {product.name} - {product.total_revenue:,.0f} VND")
    def statistics(self):
        low = 0
        medium = 0
        good = 0
        high = 0
        for product in self.products:
            if product.revenue_type == "Thấp":
                low += 1
            elif product.revenue_type == "Trung bình":
                medium += 1
            elif product.revenue_type == "Khá":
                good += 1
            else:
                high += 1
        print("Thấp:", low)
        print("Trung bình:", medium)
        print("Khá:", good)
        print("Cao:", high)

manager = ProductManager()

while True:
    print("""
        ================ MENU ================
        1. Hiển thị danh sách sản phẩm
        2. Thêm sản phẩm mới
        3. Cập nhật sản phẩm
        4. Xóa sản phẩm
        5. Tìm kiếm sản phẩm
        6. Thống kê sản phẩm
        7. Thoát
        ======================================
    """)
    choice = input("Nhập lựa chọn của bạn: ").strip()
    if choice == "1":
        manager.show_all()
    elif choice == "2":
        manager.add_product()
    elif choice == "3":
        manager.update_product()
    elif choice == "4":
        manager.delete_product()
    elif choice == "5":
        manager.search_product()
    elif choice == "6":
        manager.statistics()
    elif choice == "7":
        print("Bạn đã thoát khỏi chương trình")
        break
    else :
        print("lựa chọn không hợp lệ")
