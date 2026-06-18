# Dữ liệu từ API: (Tên, Số trận, MMR)
data = [
    ("Levi", 120, 2500),      # Dữ liệu chuẩn
    ("SofM", 150),            # Lỗi API: Bị thiếu mất trường MMR (Tuple chỉ có 2 phần tử)
    ("Optimus", 100, "N/A")   # Lỗi dữ liệu: Điểm MMR bị ghi chữ "N/A"
]

# cần hàm Tính RP thưởng cuối mùa.
def calculate_bonus(m, r):
    return (m * 10) + (r * 0.5)

# Hàm xử lý dồn cục, không có cơ chế bẫy lỗi
def process(ds):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for p in ds:
        t = p[0]
        try:
            m = p[1]
            r = p[2]
            r = int(r)
            b = calculate_bonus(m, r)
            print(f"{t}: Nhận được {b:.1f} RP")
        except IndexError:
            print(f"{t}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            print(f"{t}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue
# Chạy hệ thống
process(data)