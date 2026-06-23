def normalize_student_names(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("\n--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for student in records:
        student["name"] = " ".join(student["name"].strip().split()).title()
        print(f"{student['student_id']}: {student['name']}")
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")