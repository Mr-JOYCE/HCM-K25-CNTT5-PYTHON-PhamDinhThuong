# (1) Phân tích lỗi
#
# - Tuple product_info ban đầu có 4 phần tử:
#   ("SP001", "Áo polo nam", "Size L", 299000)
#
# - Phần tử "SP001" (mã sản phẩm) nằm ở index 0.
#   Tuy nhiên chương trình lại dùng:
#       product_code = product_info[1]
#   nên lấy nhầm phần tử ở index 1 là "Áo polo nam".
#
# - Phần tử "Áo polo nam" (tên sản phẩm) nằm ở index 1.
#   Tuy nhiên chương trình lại dùng:
#       product_name = product_info[2]
#   nên lấy nhầm phần tử ở index 2 là "Size L".
#
# - Dòng:
#       product_length = product_info.length()
#   gây lỗi vì tuple không có phương thức length().
#   Để đếm số phần tử của tuple cần sử dụng hàm len():
#       len(product_info)
#
# - Dòng:
#       product_info[3] = 279000
#   không hợp lệ vì tuple là kiểu dữ liệu bất biến (immutable),
#   không cho phép thay đổi trực tiếp giá trị của phần tử sau khi tạo.
#
# - Tuple không hỗ trợ cập nhật phần tử bằng cách gán lại theo index.
#
# - Muốn cập nhật giá bán từ 299000 thành 279000 cần tạo tuple mới,
#   ví dụ:
#       product_info = (
#           product_info[0],
#           product_info[1],
#           product_info[2],
#           279000
#       )
#   hoặc chuyển tuple sang list, sửa dữ liệu rồi tạo lại tuple.


# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm
product_code = product_info[0]

# Lấy tên sản phẩm
product_name = product_info[1]

# Đếm số lượng thông tin sản phẩm
product_length = len(product_info)

# Cập nhật giá bán
product_info = product_info[:3] + (279000,)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)