# Phân tích lỗi

# 1. Quan sát dòng gọi hàm:
# calculate_final_price(100000, 15000, 0.1)
#
# Hàm được định nghĩa:
# calculate_final_price(price, discount, shipping_fee)
#
# Python truyền tham số theo vị trí:
# price = 100000
# discount = 15000
# shipping_fee = 0.1
#
# Như vậy:
# - Giá trị 15000 đang bị gán cho tham số discount.
# - Giá trị 0.1 đang bị gán cho tham số shipping_fee.
#
# Trong khi thực tế:
# - discount phải là 0.1 (10%)
# - shipping_fee phải là 15000

# 2. Việc gán sai tham số làm công thức bị sai như thế nào?
#
# Công thức:
# total = price - (price * discount) + shipping_fee
#
# Thay giá trị thực tế mà chương trình nhận:
# total = 100000 - (100000 * 15000) + 0.1
#
# Phép nhân:
# 100000 * 15000 = 1.500.000.000
#
# Khi đó:
# total = 100000 - 1.500.000.000 + 0.1
# total = -1.499.899.999,9
#
# Kết quả trở thành số âm rất lớn vì discount bị hiểu là 15000
# thay vì 0.1 (10%).

# 3. Vì sao dòng:
# final_payment = order_total + 5000
# gây ra lỗi TypeError?
#
# Vì hàm calculate_final_price() không có return.
#
# Khi một hàm kết thúc mà không return giá trị,
# Python tự động trả về None.
#
# Lúc này:
# order_total = None
#
# Chương trình thực hiện:
# None + 5000
#
# Đây là phép cộng không hợp lệ giữa NoneType và int,
# nên Python phát sinh:
# TypeError

# 4. Biến order_total đang mang giá trị gì?
#
# order_total = None
#
# Nguyên nhân:
# Hàm chỉ dùng print(total) để hiển thị kết quả,
# nhưng không return total cho nơi gọi hàm.

# 5. Khác nhau giữa print(total) và return total?
#
# print(total):
# - Chỉ hiển thị kết quả ra màn hình.
# - Không gửi giá trị ra bên ngoài hàm.
# - Không thể dùng kết quả đó để tính toán tiếp.
#
# return total:
# - Trả kết quả về nơi gọi hàm.
# - Có thể gán cho biến:
#     order_total = calculate_final_price(...)
# - Có thể tiếp tục tính toán:
#     order_total + 5000
#
# Ví dụ:
#
# def f():
#     print(10)
#
# x = f()
# print(x)
#
# Kết quả:
# 10
# None
#
# Vì hàm không return gì nên x nhận giá trị None.

# 6. Cần sửa như thế nào?
#
# Sửa 2 lỗi:
#
# (1) Truyền tham số đúng thứ tự:
# calculate_final_price(100000, 0.1, 15000)
#
# (2) Trả kết quả bằng return:
#
# def calculate_final_price(price, discount, shipping_fee):
#     total = price - (price * discount) + shipping_fee
#     return total
#
# Sau đó:
#
# order_total = calculate_final_price(100000, 0.1, 15000)
# final_payment = order_total + 5000
#
# Tính toán:
# total = 100000 - 10000 + 15000
# total = 105000
#
# final_payment = 105000 + 5000
# final_payment = 110000
#
# Kết quả cuối cùng:
# Khách hàng cần thanh toán: 110000 VND

# Hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    print(f"Đã tính xong tổng tiền: {total:,} VND")
    return total

# Đơn hàng mua áo thun: Giá 100000, giảm giá 10% (0.1), phí ship 15000
# Gọi hàm để tính tiền
order_total = calculate_final_price(100000, 0.1, 15000)

# Hệ thống cộng thêm 5000 phí đóng gói vào tổng tiền đơn hàng
final_payment = order_total + 5000

print(f"Khách hàng cần thanh toán: {final_payment:,} VND")