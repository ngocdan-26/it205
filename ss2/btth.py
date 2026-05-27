user_name = input("nhập tên bệnh nhân: ")
date_birth = int(input("nhập năm sinh: "))
sick_day = int(input("nhập số ngày bị bệnh: "))
temperature = float(input("nhập nhiệt độ cơ thể: "))
cost = float(input("nhập chi phí khám:"))

infomaton = f"""    
                --- Kết quả ---
                Tên: {user_name}
                Năm sinh: {date_birth} 
                ngày bị bệnh: {sick_day} độ
                nhiệt độ cơ thể:{temperature}
"""

if user_name == "":
    print("tên không dược để trống!")
if date_birth < 1900 or date_birth > 2026:
    print("năm không hơp lệ!") 
if sick_day < 0:
    print("số ngày bị bệnh không hơp lệ!") 
if temperature < 30 or temperature > 45:
    print("số ngày bị bệnh không hơp lệ!") 
if cost < 0:
    print("chi phí khám không hơp lệ!")

# Tính toán thông tin
age = 2026 - date_birth

surcharge =  cost * 0.1

total_cost = cost + surcharge

#  Phân loại tình trạng sức khỏe
if temperature > 38 and sick_day > 3:
    print("Nguy hiểm")
elif temperature > 38:
    print("Sốt cao")
elif temperature >37.5:
    print("Sốt nhẹ")
else:
    print("Bình thường")

#Đánh giá mức độ ưu tiên (Nested If)
if temperature > 38 and sick_day > 3 :
    if age > 60:
        print("Cấp cứu")
    else :
        print("Ưu tiên cao")
else:
    print("Bình thường")

#Đánh giá mức chi phí (Toán tử 3 ngôi)
envaluation = "Cao" if total_cost > 500000 else "Thap"
print(envaluation)
