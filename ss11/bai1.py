# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm
# mã sp phải là 0
product_code = product_info[0]

# Lấy tên sản phẩm
# tên sp phải là 1
product_name = product_info[1]

# Đếm số lượng thông tin sản phẩm
# sd len() để đếm sl thông tin sp
product_length = len(product_info)

# Cập nhật giá bán
new_product_info = product_info[:3] + (279000,)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", new_product_info)