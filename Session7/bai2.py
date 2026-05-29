# PHÂN TÍCH LỖI CHƯƠNG TRÌNH

# 1. Vì sao transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu?
# Vì trong Python, chuỗi (string) là immutable (không thể thay đổi trực tiếp).
#
# Phương thức strip() chỉ tạo ra một chuỗi mới đã xóa khoảng trắng,
# nhưng chương trình không gán lại kết quả vào biến transaction.
#
# Ví dụ đúng:
# transaction = transaction.strip()


# 2. Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?
# Dữ liệu transaction được phân tách bằng dấu "|"
#
# Ví dụ:
# " nguyEN vAn a | PYTHON-01 | 15000000 | paid "
#
# Các phần dữ liệu:
# - Họ tên
# - Mã khóa học
# - Số tiền
# - Trạng thái
#
# đều được ngăn cách bằng "|"


# 3. Vì sao transaction.split("-") là sai?
# Vì dấu "-" không phải delimiter chính của chuỗi.
#
# Trong dữ liệu:
# "PYTHON-01"
#
# dấu "-" chỉ là một phần của mã khóa học,
# không phải ký tự dùng để tách dữ liệu giao dịch.
#
# Khi split("-"),
# Python sẽ tách sai dữ liệu.


# 4. Sau khi tách sai delimiter, dữ liệu trong parts bị lệch như thế nào?
# Ví dụ:
#
# transaction.split("-")
#
# sẽ cho kết quả gần giống:
#
# parts[0] = " nguyEN vAn a | PYTHON"
# parts[1] = "01 | 15000000 | paid "
#
# Lúc này:
# - parts chỉ có 2 phần
# - nhưng chương trình lại truy cập:
#   parts[2]
#   parts[3]
#
# nên sẽ gây lỗi:
#
# IndexError: list index out of range


# 5. Vì sao cần .strip() lại từng phần sau khi split()?
# Vì sau khi split("|"),
# dữ liệu vẫn còn khoảng trắng dư thừa.
#
# Ví dụ:
#
# parts[0]
# có thể là:
# " nguyEN vAn a "
#
# Nếu không strip():
# - dữ liệu hiển thị sẽ bị dư khoảng trắng
# - title(), upper() hoặc lower()
#   sẽ xử lý không sạch dữ liệu
#
# Ví dụ đúng:
#
# student_name = parts[0].strip().title()


# 6. Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng tiền?
# Sau khi split(),
# amount vẫn là kiểu str.
#
# Ví dụ:
# amount = "15000000"
#
# Nếu không chuyển sang int hoặc float:
# - không thể tính toán
# - không thể format tiền chuyên nghiệp
#
# Ví dụ:
#
# amount = int(parts[2].strip())
#
# Sau đó mới có thể:
#
# print(f"Số tiền: {amount:,} VND")
#
# Kết quả:
# 15,000,000 VND
#
# Nếu vẫn là chuỗi,
# dữ liệu chỉ được in ra như văn bản thông thường.

transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

# 1. Xóa khoảng trắng thừa ở hai đầu
transaction = transaction.strip()

# 2. Tách chuỗi theo ký tự phân cách đúng
parts = transaction.split("|")

# 3. Chuẩn hóa riêng từng phần dữ liệu
student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount_str = parts[2].strip()
status = parts[3].strip().upper()

# 4. Chuyển số tiền sang số nguyên trước khi định dạng
amount = int(amount_str)
formatted_amount = f"{amount:,}"

# 5. In báo cáo theo định dạng yêu cầu
print(f"Học viên: {student_name}")
print(f"Khóa học: {course_code}")
print(f"Số tiền: {formatted_amount} VND")
print(f"Trạng thái: {status}")
