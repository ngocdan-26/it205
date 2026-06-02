# câu 1:
print("Câu 1: ")
price = int(input("nhập vào Đơn giá của một sản phẩm: "))
quantity = int(input("nhập vào Số lượng mua: "))
total = price * quantity
if total >= 1000000:
    total = total - total * 0.1
print(f"Số tiền cuối cùng khách phải thanh toán: {total}")

# câu 2:
print("Câu 2: ")
password = "123456"
cost = 0
while True:
    cost += 1
    is_password = input("nhập mật khẩu: ")
    if  password == is_password:
        print("Đăng nhập thành công!")
        break
    else:
        if cost == 3:
            print( "Tài khoản đã bị khóa!")
            break
        print("Mật khẩu sai, vui lòng nhập lại!")
    

# câu 3:
print("Câu 3: ")
total_product = 0
valid_packages = 0
while True:
    quantity = int(input("nhập số lượng của từng thùng: "))
    if quantity < 0 :
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
    elif quantity > 0 :
        valid_packages += 1
        total_product += quantity
    else:
        break
    
print(f"Tổng số thùng hàng hợp lệ đã đếm: {valid_packages}")
print(f"Tổng số lượng sản phẩm thu được: {total_product}")