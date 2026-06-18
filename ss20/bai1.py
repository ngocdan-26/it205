# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
data = [
    ("Faker", "10", "2", "8"),      # Tuyển thủ 1: Dữ liệu bình thường
    ("ShowMaker", "15", "0", "10"), # Tuyển thủ 2: Không chết mạng nào (Deaths = 0)
    ("Chovy", "12", "ba", "5")      # Tuyển thủ 3: Lỗi API trả về chữ 'ba' thay vì số 3
]

# Cần tạo 1 hàm tính toán kda
def calculate_kda(k, d, a):
    return (k + a) / d

# Hàm xử lý dồn cục, đặt tên biến kém
def tinh_toan(ds):
    print("--- BẢNG XẾP HẠNG KDA ---")
    for x in ds:
        n = x[0]
        k = x[1]
        d = x[2]
        a = x[3]
        
        # dùng try để hiển thị ra kết quả
        try:
            k = int(k)
            d= int(d)
            a= int(a)

            kda = calculate_kda(k,d,a)
            print(f"{n}: KDA = {kda:.2f}")

        except ZeroDivisionError:
            print(f"{n}: KDA Hoàn hảo (Perfect Game)!" )
            continue

        except ValueError:
            print(f"{n}: Lỗi dữ liệu không hợp lệ!")
            continue


# Chạy hệ thống
tinh_toan(data)