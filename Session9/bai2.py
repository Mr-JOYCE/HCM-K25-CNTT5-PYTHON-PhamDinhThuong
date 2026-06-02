# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai (tìm theo giá trị, không dùng chỉ số cố định)
try:
	idx = express_orders.index("GE102-WRONG")
	express_orders[idx] = "GE102-UPDATED"
except ValueError:
	pass

# Xóa đơn hàng bị khách hủy theo giá trị (remove sẽ loại phần tử đầu khớp)
try:
	express_orders.remove("GE103-CANCEL")
except ValueError:
	pass

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)