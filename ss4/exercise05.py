customer = 1
total_revenue = 0
large_bill = 0
while True:
    bill = int(input(f"Khách hàng {customer} Nhập giá trị hóa đơn: "))
    total_revenue += bill
    if bill > 1000000:
        large_bill += 1
    choice = input("Có muốn nhập tiếp không? (C/K): ")
    if choice == "c" :
        customer += 1
    if choice == "k" :
        break
bill_ratio = large_bill / customer * 100
print (f"""
            --- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---
            Tổng số hóa đơn đã xử lý: {customer} hóa đơn.
            Tổng doanh thu ngày hôm nay: {total_revenue} VND.
            Số hóa đơn lớn (≥ 1,000,000 VND): {large_bill} hóa đơn.
            Tỷ lệ hóa đơn lớn đạt: {bill_ratio}% trên tổng số đơn hàng.
""")