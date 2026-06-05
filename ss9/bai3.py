# Input/Output
# Input: lựa chọn menu, mã đơn hàng nhập từ bàn phím 
# Output: danh sách đơn hàng hiển thị, thông báo thêm/xóa thành công hoặc lỗi, thông báo thoát chương trình.

order_list = ["GE001", "GE002", "GE003"]

while True:
    print("""
        ===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
        1. Hiển thị danh sách đơn hàng
        2. Thêm đơn hàng mới
        3. Xóa đơn hàng theo mã
        4. Thoát chương trình
        """)
    choice = int(input("Nhập lựa chọn của bạn: "))
    match choice:
        case 1:
            if len(order_list) == 0:
                print("Đơn hàng đang trống")
            else:
                print("Danh sách đơn hàng hiện tại: ")
                for i, order in enumerate(order_list, start= 1):
                    print(f"{i}. {order}")
        case 2:
            new_order = input("Nhập mã đơn hàng mới: ").strip().upper()
            order_list.append(new_order)
        case 3:
            delete_order = input("Nhập mã đơn hàng cần xóa: ").strip().upper()
            if delete_order in order_list:
                order_list.remove(delete_order)
            else:
                print("Không tìm thấy đơn hàng cần xóa")
        case 4:
            print("Thoát chương trình")
            break
        case _ :
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại")
            
            