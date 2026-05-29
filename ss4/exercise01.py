pirce = int(input("Nhập tổng tiền hóa đơn ban đầu: "))
if pirce < 0:
    print("tổng tiền nhập không phù hợp!")
elif pirce < 500000:
    print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
    print(f"Tổng tiền khách phải trả: {pirce} VND")
else:
    print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
    print(f"Số tiền được giảm giá: {pirce * 0.1} VND")
    print(f"Tổng tiền khách phải trả: {pirce - pirce * 0.1} VND")