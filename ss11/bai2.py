# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
# kh lấy đc mã khi để 0 phải lấy ra key
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên 
# để key sai phải đổi thành full_name
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên
# key sai tên sửa lại thành status
employee["status"] = "official"

# Thêm lương cơ bản
# employee.append("base_salary", 15000000)
#Thay append() bằng cú pháp gán key mới
employee["base_salary"] = 15000000

# Xóa phòng ban
# Sửa lại key thành department
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)