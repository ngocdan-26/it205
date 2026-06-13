patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def validate_gender(gender_input):
    gender = gender_input.strip().lower()
    return gender in ["nam", "nu"]

def find_patient_index(patient_list, patient_id):
    patient_id = patient_id.strip().upper()
    for index, patient in enumerate(patient_list):
        if patient[0] == patient_id:
            return index
    return -1

def display_patients(patient_list):
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    for i, patient in enumerate(patient_list, start=1):
        print(f"{i}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")

def add_patient(patient_list):
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if not patient_id:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return
    patient_name = input("Nhập tên bệnh nhân: ").strip()
    if not patient_name:
        print("Tên bệnh nhân không được để trống!")
        return
    patient_name = patient_name.title()
    while True:
        gender_input = input("Nhập giới tính Nam/Nu: ")
        if validate_gender(gender_input):
            gender = gender_input.strip().lower().capitalize()
            break
        print("Giới tính không hợp lệ, vui lòng nhập lại!")
    disease = input("Nhập chẩn đoán bệnh: ").strip()
    if not disease:
        print("Chẩn đoán bệnh không được để trống!")
        return
    disease = disease.capitalize()
    patient_list.append(
        [
            patient_id,
            patient_name,
            gender,
            disease
        ]
    )
    print("Tiếp nhận bệnh nhân thành công!")

def update_diagnosis(patient_list):
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    if not patient_id:
        print("Mã bệnh nhân không được để trống!")
        return
    index = find_patient_index(patient_list, patient_id)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return
    patient = patient_list[index]
    print(f"Tìm thấy bệnh nhân: {patient[1]}")
    print(f"Chẩn đoán hiện tại: {patient[3]}")
    new_disease = input("Nhập chẩn đoán mới: ").strip()
    if not new_disease:
        print("Chẩn đoán bệnh không được để trống!")
        return
    patient_list[index][3] = new_disease.capitalize()
    print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list):
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = input("Nhập từ khóa tên bệnh: ").strip()
    if not keyword:
        print("Từ khóa tìm kiếm không được để trống!")
        return
    count = 0
    print("Kết quả tìm kiếm:")
    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            count += 1

            print(f"{count}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(f"Có tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'." )

def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    print("===========================================")


while True:
    display_menu()

    choice = input("Nhập lựa chọn của bạn: ").strip()

    if choice == "1":
        display_patients(patients)

    elif choice == "2":
        add_patient(patients)

    elif choice == "3":
        update_diagnosis(patients)

    elif choice == "4":
        search_by_disease(patients)

    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")