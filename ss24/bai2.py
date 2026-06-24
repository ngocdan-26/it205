# Hệ thống Thẻ thành viên Rikkei Coffee
class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = 0
        self.points = points  # Lỗ hổng 1: Thuộc tính public, không có kiểm duyệt

    @property
    def points(self):
        return self.__points
    
    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount

    # Lỗ hổng 2: Hàm tiện ích nhưng lại bị ép phải dùng 'self'
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000

# --- KỊCH BẢN THAO TÁC LỖI CỦA THU NGÂN ---

card1 = MemberCard("Le Van C", 100)
print("Điểm ban đầu:", card1.points)
# 1. Thu ngân gõ nhầm, gán điểm thành số âm hoặc chuỗi
card1.points = -50 
# card1.points = "một trăm" (Sẽ gây crash hệ thống nếu chạy)
print("Điểm sau khi gán sai:", card1.points)
# 2. Thu ngân muốn kiểm tra nhanh một hóa đơn 250k có được tặng voucher không
# Phải gọi qua object card1 (rất vô lý vì hóa đơn này của một khách vãng lai)
result = MemberCard.is_eligible_for_voucher(250000)

# Nếu thu ngân cố tình gọi trực tiếp từ Class sẽ bị lỗi TypeError:
# MemberCard.is_eligible_for_voucher(250000) 

print(f"Khách hàng: {card1.customer_name}")
print(f"Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250k có được tặng Voucher không? {result}")