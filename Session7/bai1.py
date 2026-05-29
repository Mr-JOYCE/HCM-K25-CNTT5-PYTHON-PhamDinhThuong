# PHÂN TÍCH LỖI CHƯƠNG TRÌNH

# 1. Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?
# Vì các phương thức xử lý chuỗi trong Python như strip(), title(), upper(), lower()
# KHÔNG thay đổi dữ liệu gốc.
# Chúng chỉ tạo ra một chuỗi mới sau khi xử lý.
#
# Ví dụ:
# student_name.strip()
# chỉ trả về kết quả đã xóa khoảng trắng,
# nhưng không gán lại vào biến student_name,
# nên giá trị ban đầu vẫn giữ nguyên.


# 2. Vì sao student_name.title() không tạo ra kết quả "Nguyen Van A"?
# Vì kết quả của title() không được lưu lại.
#
# student_name.title()
# chỉ tạo chuỗi mới:
# "Nguyen Van A"
#
# nhưng chương trình không:
# student_name = student_name.title()
#
# nên biến student_name vẫn giữ giá trị cũ:
# "  nguYEn vAn a  "


# 3. Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?
# Vì phương thức upper() cũng hoạt động giống strip() và title().
#
# Nó chỉ trả về chuỗi mới đã viết hoa,
# nhưng không cập nhật trực tiếp vào biến student_code.
#
# Do không gán lại:
# student_code = student_code.upper()
#
# nên dữ liệu không thay đổi.


# 4. Vì sao email.lower() không làm email chuyển thành chữ thường?
# Vì lower() chỉ sinh ra chuỗi mới ở dạng chữ thường.
#
# Chương trình hiện tại không lưu kết quả đó vào biến email,
# nên email vẫn giữ nguyên giá trị ban đầu.


# 5. Muốn các phương thức xử lý chuỗi có hiệu lực cần làm gì?
# Cần GÁN LẠI kết quả xử lý vào biến.
#
# Ví dụ đúng:
#
# student_name = student_name.strip().title()
#
# student_code = student_code.strip().upper()
#
# email = email.strip().lower()
#
# Khi đó:
# - Khoảng trắng được xóa
# - Chữ hoa/thường được chuẩn hóa
# - Dữ liệu trong biến mới thực sự thay đổi


student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)