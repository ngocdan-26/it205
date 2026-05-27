user_name = input("nhập tên bệnh nhân: ")
gender = input("nhập giới tính: ")
date_birth = int(input("nhập năm sinh: "))
phone_number = input("nhập số điện thoai: ")
email = input("nhập email: ")
symptoms = ("nhập triệu chứng ban đầu")
cost = float(input("nhập chi phí khám: "))
random = int(input("nhập 3 số ngẫu nhiên: "))
code = f"BN{date_birth}{random}"

print("--- thẻ bệnh nhân ---")
infomaton = f"""    
                Mã BN: {code} 
                Tên: {user_name}
                Giới tính: {gender} 
                Năm sinh:{date_birth} 
                Sdt:{phone_number} 
                Triệu chứng: {symptoms}
                Chi phí: {cost}
"""
print(infomaton)