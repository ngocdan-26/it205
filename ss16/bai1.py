# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]
# Hàm chuẩn hóa tên bệnh và thêm vào hồ sơ
def add_diagnosis(raw_diagnosis, current_list):
    # Cố gắng chuẩn hóa tên bệnh
    # phải gán dữ liệu với dữ liệu đã chuẩn hóa
    raw_diagnosis = raw_diagnosis.strip()
    raw_diagnosis = raw_diagnosis.title()
    # Thêm chẩn đoán vào danh sách bệnh án
    # phải sd append để thêm vào danh sách
    current_list.append(raw_diagnosis)
    return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Gọi hàm để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)