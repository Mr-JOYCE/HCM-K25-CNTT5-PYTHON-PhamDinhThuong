# =========================
# Phân tích lỗi
# =========================

# 1. Biến total_points được khai báo ở dòng 2 là biến toàn cục (Global)
# hay cục bộ (Local)? Tại sao?
#
# total_points = 100
#
# Đây là biến toàn cục (Global Variable) vì nó được khai báo bên ngoài
# tất cả các hàm và có thể được truy cập từ nhiều nơi trong chương trình.
#
# Phạm vi hoạt động (scope) của nó là toàn bộ file chương trình.

# 2. Giải thích lỗi:
# UnboundLocalError:
# local variable 'total_points' referenced before assignment
#
# Bên trong hàm:
#
# def add_reward_points(points_earned):
#     total_points = total_points + points_earned
#
# Python nhìn thấy phép gán:
#
# total_points = ...
#
# nên Python mặc định hiểu rằng total_points bên trong hàm là
# một biến cục bộ (local variable).
#
# Tương đương cách hiểu của Python:
#
# def add_reward_points(points_earned):
#     local_total_points = local_total_points + points_earned
#
# Nhưng trước khi biến local này được gán giá trị,
# chương trình lại cố đọc nó ở vế phải:
#
# total_points + points_earned
#
# nên Python báo lỗi:
#
# "Biến cục bộ total_points đang được sử dụng trước khi được gán giá trị."

# 3. Nếu chỉ đọc (print) biến total_points bên trong hàm thì có lỗi không?
#
# Ví dụ:
#
# total_points = 100
#
# def show_points():
#     print(total_points)
#
# show_points()
#
# Kết quả:
# 100
#
# Chương trình KHÔNG bị lỗi.
#
# Lý do:
# Khi chỉ đọc dữ liệu, Python sẽ tìm biến theo thứ tự:
# Local -> Global.
#
# Không tìm thấy biến local thì Python sẽ sử dụng biến global.

# 4. Cách sửa 1:
# Dùng từ khóa global
#
# Từ khóa:
# global
#
# giúp Python hiểu rằng:
# "Hãy sử dụng biến toàn cục bên ngoài,
# không tạo biến cục bộ mới."
#
# Ví dụ:

# total_points = 100
#
# def add_reward_points(points_earned):
#     global total_points
#     total_points = total_points + points_earned
#     print("Đã cộng thêm", points_earned, "điểm.")

#
# Sau khi gọi:
#
# add_reward_points(50)
#
# total_points sẽ trở thành:
# 150

# 5. Cách sửa 2 (Clean Code hơn - Khuyến nghị)
#
# Không nên để hàm thay đổi trực tiếp biến toàn cục.
#
# Một hàm tốt nên:
# - Nhận dữ liệu đầu vào bằng tham số.
# - Tính toán.
# - return kết quả.
#
# Từ khóa cần dùng:
# return
#
# Ví dụ:

# def add_reward_points(current_points, points_earned):
#     return current_points + points_earned
#
# total_points = 100
#
# total_points = add_reward_points(total_points, 50)
#
# print(total_points)

#
# Luồng xử lý:
#
# current_points = 100
# points_earned = 50
#
# return 150
#
# total_points nhận giá trị 150
#
# Ưu điểm:
# - Dễ kiểm thử (test).
# - Ít gây lỗi ngoài ý muốn.
# - Không phụ thuộc biến toàn cục.
# - Dễ bảo trì khi dự án lớn.

# =========================
# Kết luận
# =========================
#
# Nguyên nhân lỗi:
# Python thấy có phép gán:
# total_points = ...
# nên coi total_points trong hàm là biến local.
#
# Khi đọc:
# total_points + points_earned
# thì biến local chưa có giá trị => UnboundLocalError.
#
# Có 2 cách sửa:
#
# 1. Dùng global total_points.
#
# 2. Tốt hơn: truyền total_points vào hàm và
#    dùng return để trả về kết quả mới.


# Biến toàn cục lưu tổng điểm hiện tại của khách hàng
total_points = 100

# Hàm cộng điểm thưởng
def add_reward_points(current_points, points_earned):
    global total_points  # Sử dụng biến toàn cục để cập nhật tổng điểm
    # Cố gắng lấy tổng điểm cũ cộng thêm điểm mới
    total_points = current_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")

# Khách mua hàng được thưởng 50 điểm
add_reward_points(total_points, 50)

# In ra kết quả
print("Tổng điểm hiện tại của khách hàng:", total_points)