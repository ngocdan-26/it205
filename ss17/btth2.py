students = [{
    "id": "SV001",
    "full_name": "Nguyen Van A",
    "math_scores": 8.5,
    "physics_scores": 7.0,
    "chemistry_scores": 9.0,
    "avg": 8.17,
    "rating": "Giỏi"
}]

# students = []
def rating_student(avg):
    if avg < 5:
        rating = "Yếu"
    elif avg < 7:
        rating = "Trung bình"
    elif avg < 8 :
        rating = "Khá"
    else:
        rating = "Giỏi"
    return rating

def display_student(student):
    if not students:
            print("Hệ thống không có dữ liệu sinh viên")
    else:
        print("---- Danh scahs hiển thị sinh viên ----")
        print("id | Họ và tên | Điểm toán | Điểm lý | Điểm hóa | Điểm trung bình | Xếp loại")
        for  stu in student:
            print(f"{stu["id"]} | {stu["full_name"]} | {stu["math_scores"]} | {stu["physics_scores"]} | {stu["chemistry_scores"]} | {stu["avg"]} | {stu["rating"]}")

def add_student(student):
    id = input("Nhập mã sinh viên: ").strip().upper()
    if not id :
        print("Mã sinh viên không được rỗng.")
        return
    for stu in student:
        if stu["id"] == id:
            print("Mã sinh viên không được trùng")
            return
    name = input("Nhập họ và tên sinh viên: ").strip().title()
    if not name:
        print("Tên sinh viên không được rỗng")
        return
    avg = 0
    math = input("Nhập điểm toán: ").strip()
    physics = input("Nhập điểm lý: ").strip()
    chemistry = input("Nhập điểm hóa: ").strip()
    if math.replace(".","").isdigit() and physics.replace(".","").isdigit() and chemistry.replace(".","").isdigit():
        math_scores = float(math)   
        physics_scores = float(physics)
        chemistry_scores = float(chemistry)
        if 0 <= math_scores <= 10 and 0<= physics_scores <= 10 and 0<= chemistry_scores <= 10:
            avg = (math_scores + physics_scores + chemistry_scores) / 3
        else:
            print("Điểm số phải là số hợp lệ trong khoảng từ 0 đến 10")
            return
    rating = rating_student(avg)
    new_student = {
        "id": id,
        "full_name": name,
        "math_scores": math_scores,
        "physics_scores": physics_scores,
        "chemistry_scores": chemistry_scores,
        "avg": avg,
        "rating": rating
    }
    student.append(new_student)
    print("them sv thanh cong")

def update_student(student):
    check_id = input("Nhập mã sinh viên cần tìm: ").strip().upper()
    if not check_id:
        print("Hệ thống không có dữ liệu sinh viên")
    for stu in student:
        if check_id == stu["id"]:
            new_avg = 0
            math = input("Nhập điểm toán mới: ").strip()
            physics = input("Nhập điểm lý mới: ").strip()
            chemistry = input("Nhập điểm hóa mới: ").strip()
            if math.replace(".","").isdigit() and physics.replace(".","").isdigit() and chemistry.replace(".","").isdigit():
                new_math = float(math)   
                new_physics = float(physics)
                new_chemistry = float(chemistry)
                if 0 <= new_math <= 10 and 0<= new_physics <= 10 and 0<= new_chemistry <= 10:
                    new_avg = (new_math + new_physics + new_chemistry) / 3
                else:
                    print("Điểm số phải là số hợp lệ trong khoảng từ 0 đến 10")
                    return
            new_rating = rating_student(new_avg)
            stu["math_scores"] = new_math
            stu["physics_scores"] = new_physics
            stu["chemistry_scores"] = new_chemistry
            stu["avg"] = new_avg
            stu["rating"] = new_rating
            print(f"đã cập nhật điểm cho sv:{check_id} thành công.")
    print("mã sv không hợp lệ")   
    
def delete_students(student):
    check_id = input("Nhập mã sinh viên cần tìm: ").strip().upper()
    if not check_id:
        print("Hệ thống không có dữ liệu sinh viên")
    for stu in student:
        if stu["id"] == check_id:
            check = input("Bạn có chắc muốn xóa? (yes/no): ").strip().lower()
            if check == "yes":
                print("bạn đã xóa sinh viên khỏi danh sách")
                student.remove(stu)
                return
            elif check == "no":
                print("bạn đã từ chối xóa nhân viên")
                return
    print("mã sv không hợp lệ")   

def search_student(student):
    check = input("bạn muốn tìm sinh viên bằng mã hay tên (id/name): ").strip().lower()
    if check == "id":
        check_id = input("Nhập mã sinh viên cần tìm: ").strip().upper()
        for stu in student:
            if stu["id"] == check_id:
                print("id | Họ và tên | Điểm toán | Điểm lý | Điểm hóa | Điểm trung bình | Xếp loại")
                print(f"{stu["id"]} | {stu["full_name"]} | {stu["math_scores"]} | {stu["physics_scores"]} | {stu["chemistry_scores"]} | {stu["avg"]} | {stu["rating"]}")
   
    elif check == "name":
        check_name = input("nhập tên sinh viên cần tìm: ").strip().lower().title()
        for stu in student:
            if stu["full_name"] == check_name:
                print("id | Họ và tên | Điểm toán | Điểm lý | Điểm hóa | Điểm trung bình | Xếp loại")
                print(f"{stu["id"]} | {stu["full_name"]} | {stu["math_scores"]} | {stu["physics_scores"]} | {stu["chemistry_scores"]} | {stu["avg"]} | {stu["rating"]}")
    else:
        print("lua chon khong hop le")

def statistics(student):
    gioi = 0
    kha = 0
    trung_binh = 0
    yeu = 0

    for stu in student:
        if stu["rating"] == "Giỏi":
            gioi += 1
        elif stu["rating"] == "Khá":
            kha += 1
        elif stu["rating"] == "Trung bình":
            trung_binh += 1
        else:
            yeu += 1

    print("--- THỐNG KÊ HỌC LỰC ---")
    print(f"Giỏi: {gioi}")
    print(f"Khá: {kha}")
    print(f"Trung bình: {trung_binh}")
    print(f"Yếu: {yeu}")
     

while True:
    print("""
        ----- Hệ thống đào tạo quản lý danh sách sinh viên -----
                1. Hiển thị danh sách sinh viên
                2. Tiếp nhận sinh viên
                3. Cập nhật kết quả học tập
                4. Xoá sinh viên
                5. Tìm kiếm sinh viên
                6. Thống kê điểm TB
                7. Thoát hệ thống
""")

    choice = input("lựa chọn chức năng(1-7): ")
    if choice == "1":
        display_student(students)
    elif choice == "2":
        add_student(students)
    elif choice =="3":
        update_student(students)
    elif choice == "4":
        delete_students(students)
    elif choice == "5":
        search_student(students)
    elif choice =="6":
        statistics(students)
    elif choice == "7":
        print("Bạn đã thoát khỏi chương trình.")
        break 
    else:
        print("lựa chọn không hợp lệ")