# (1) Phân tích lỗi
#
# - Dictionary employee gồm các key:
#   "employee_id", "full_name", "department", "status"
#
# - Dòng:
#       employee_id = employee[0]
#   gây lỗi vì dictionary không truy cập dữ liệu bằng index như list hoặc tuple.
#
# - Dictionary sử dụng key để truy cập giá trị, không sử dụng vị trí phần tử.
#
# - Muốn lấy mã nhân viên "NV001" cần dùng:
#       employee["employee_id"]
#
# - Dòng:
#       full_name = employee["name"]
#   gây lỗi vì key "name" không tồn tại trong dictionary.
#
# - Key đúng để lấy họ tên nhân viên là:
#       "full_name"
#
# - Dòng:
#       employee["employee_status"] = "official"
#   không cập nhật đúng trạng thái nhân viên vì key "employee_status"
#   chưa tồn tại trong dictionary.
#   Lệnh này sẽ tạo thêm một key mới thay vì cập nhật key cũ.
#
# - Key đúng để cập nhật trạng thái nhân viên là:
#       "status"
#
# - Dòng:
#       employee.append("base_salary", 15000000)
#   gây lỗi vì dictionary không có phương thức append().
#
# - append() chỉ được sử dụng với list để thêm phần tử vào cuối danh sách.
#
# - Muốn thêm lương cơ bản base_salary bằng 15000000 cần viết:
#       employee["base_salary"] = 15000000
#
# - Dòng:
#       del employee["team"]
#   gây lỗi vì key "team" không tồn tại trong dictionary.
#
# - Muốn xóa thông tin phòng ban cần dùng key:
#       "department"
#
#   Ví dụ:
#       del employee["department"]

# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên
employee["status"] = "official"

# Thêm lương cơ bản
employee["base_salary"] = 15000000

# Xóa phòng ban
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)