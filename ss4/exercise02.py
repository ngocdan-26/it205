total_revenue = 0
number_today = 0
for i in range(1,8):
    revenue = int(input(f"Nhập doanh thu Ngày {i}: "))
    total_revenue += revenue
    if revenue >= 5000000:
        number_today += 1

avg_revenue = total_revenue / 7
infomaton = f"""
                --- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---
                Tổng doanh thu cả tuần: {total_revenue} VND
                Doanh thu trung bình mỗi ngày: {avg_revenue} VND
                Số ngày đạt doanh thu mục tiêu (≥ 5,000,000 VND): {number_today} ngày
"""
print(infomaton)