import logging

# Cấu hình hệ thống Logging ban đầu theo yêu cầu
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def show_devices(devices):
    """
    Chức năng 1: Xem danh sách thiết bị giám sát hiện có.
    Duyệt dữ liệu và in bảng căn lề thẳng hàng bằng kỹ thuật f-string.
    """
    if not devices:
        print("\n--- HỆ THỐNG TRỐNG (Không có thiết bị nào) ---")
        return
    
    print("\n" + "-"*85)
    print(f"{'Mã TB':<10} | {'Vị trí xưởng':<25} | {'Chỉ số cũ':<12} | {'Chỉ số mới':<12} | {'Trạng thái':<15}")
    print("-"*85)
    for dev in devices:
        print(f"{dev['id']:<10} | {dev['location']:<25} | {dev['old_index']:<12} | {dev['new_index']:<12} | {dev['status']:<15}")
    print("-"*85)


def update_indices(devices):
    """
    Chức năng 2: Cập nhật chỉ số điện tiêu thụ (Check-in số liệu).
    Thực hiện validate dữ liệu nhập và kiểm tra mã định danh.
    """
    print("\n--- CẬP NHẬT CHỈ SỐ ĐIỆN ---")
    device_id = input("Nhập mã thiết bị cần cập nhật: ").strip()
    
    # Tìm kiếm thiết bị theo mã ID
    device = next((d for d in devices if d['id'] == device_id), None)
    if not device:
        print(f"Lỗi: ERR-E01 - Không tìm thấy mã thiết bị '{device_id}' trong hệ thống!")
        return

    # Vòng lặp validate thông tin nhập vào cho đến khi hợp lệ
    while True:
        try:
            # Nếu người dùng nhấn Enter, lấy lại giá trị cũ hiện tại
            old_idx_input = input(f"Nhập chỉ số cũ hiện tại ({device['old_index']}): ").strip()
            old_idx = int(old_idx_input) if old_idx_input else device['old_index']
            
            new_idx = int(input("Nhập chỉ số mới: ").strip())
            
            if old_idx < 0 or new_idx < 0:
                print("Lỗi: Chỉ số phải là số lớn hơn hoặc bằng 0. Vui lòng nhập lại!")
                continue
                
            if new_idx < old_idx:
                print(f"Lỗi: ERR-E02 - Chỉ số mới ({new_idx}) không được nhỏ hơn chỉ số cũ ({old_idx})! Vui lòng nhập lại.")
                continue
                
            # Tiến hành cập nhật trực tiếp vào dictionary của list gốc
            device['old_index'] = old_idx
            device['new_index'] = new_idx
            print(f" Cập nhật chỉ số thành công cho thiết bị {device_id}!")
            break
        except ValueError:
            print("Lỗi: Chỉ số điện phải là ký tự số nguyên! Vui lòng nhập lại.")


def activate_warning(devices):
    """
    Chức năng 3: Kích hoạt trạng thái cảnh báo quá tải.
    Chuyển trạng thái sang 'Overload' và ghi nhận LOG ở mức WARNING nếu tiêu thụ > 5000 kWh.
    """
    print("\n--- KÍCH HOẠT CẢNH BÁO QUÁ TẢI ---")
    device_id = input("Nhập mã thiết bị cần duyệt cảnh báo: ").strip()
    
    device = next((d for d in devices if d['id'] == device_id), None)
    if not device:
        print(f"Lỗi: ERR-E01 - Không tìm thấy mã thiết bị '{device_id}'!")
        return
        
    if device['status'] == 'Overload':
        print(f"Lỗi: ERR-E04 - Thiết bị '{device_id}' đã ở trạng thái Overload từ trước!")
        return
        
    # Tính toán lượng điện tiêu thụ của thiết bị
    consumption = device['new_index'] - device['old_index']
    if consumption > 5000:
        device['status'] = 'Overload'
        print(f" Kích hoạt trạng thái quá tải cho thiết bị {device_id} thành công!")
        # Phát thông báo log mức WARNING ra hệ thống console
        logging.warning(f"Thiết bị {device_id} tại {device['location']} tiêu thụ vượt ngưỡng ({consumption} kWh) -> Chuyển sang OVERLOAD!")
    else:
        print(f"Thiết bị {device_id} hoạt động bình thường (Tiêu thụ: {consumption} kWh <= 5000 kWh).")


def calculate_energy_financials(devices):
    """
    Chức năng 4: Tính tổng lượng điện & Chi phí năng lượng.
    Hàm này CHỈ tính toán và RETURN một Tuple chứa 3 giá trị theo đúng SRS:
    (tổng lượng điện tiêu thụ, phần trăm chiết khấu, tổng tiền sau chiết khấu)
    """
    base_price = 3000  # Đơn giá cơ sở: 3,000 VND / kWh
    total_consumption = 0
    
    for dev in devices:
        total_consumption += (dev['new_index'] - dev['old_index'])
        
    # Xác định mức chiết khấu áp dụng theo tổng sản lượng
    if total_consumption >= 50000:
        discount_rate = 0.03  # 3% Chiết khấu
    else:
        discount_rate = 0.0   # 0% Chiết khấu
        
    total_before_discount = total_consumption * base_price
    total_after_discount = total_before_discount * (1 - discount_rate)
    
    return (total_consumption, int(discount_rate * 100), int(total_after_discount))


def main():
    """Hàm điều phối chính (Hàm main) điều hướng menu chức năng"""
    # Khởi tạo danh sách thiết bị chạy demo theo mẫu SRS
    devices = [
        {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'}
    ]
    
    while True:
        print("\n" + "-"*15 + " SMART ENERGY MONITOR MENU " + "-"*15)
        print("1. Xem danh sách thiết bị giám sát hiện có")
        print("2. Cập nhật chỉ số điện tiêu thụ (Check-in số liệu)")
        print("3. Kích hoạt trạng thái cảnh báo quá tải")
        print("4. Tính tổng lượng điện & Chi phí năng lượng")
        print("5. Thoát chương trình")
        print("-"*57)
        
        try:
            choice = int(input("Mời chọn chức năng (1-5): ").strip())
            
            if choice == 1:
                show_devices(devices)
            elif choice == 2:
                update_indices(devices)
            elif choice == 3:
                activate_warning(devices)
            elif choice == 4:
                # Gọi hàm tính toán nhận Tuple và hiển thị kết quả tại đây
                total_kwh, discount, total_money = calculate_energy_financials(devices)
                print("\n" + "—"*10 + " BÁO CÁO TÀI CHÍNH NĂNG LƯỢNG " + "—"*10)
                print(f"+ Tổng lượng điện tiêu thụ thực tế: {total_kwh:,} kWh")
                print(f"+ Tỷ lệ chiết khấu áp dụng từ nhà nước: {discount}%")
                print(f"+ Tổng chi phí năng lượng phải trả sau chiết khấu: {total_money:,} VND")
                print("—"*50)
            elif choice == 5:
                print("\nCảm ơn bạn đã sử dụng phần mềm Smart Energy Monitor! Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn số từ 1 đến 5.")
                
        except ValueError:
            print("Lỗi: Vui lòng nhập ký tự số (1-5), không nhập chữ hoặc ký tự đặc biệt!")

if __name__ == "__main__":
    main()