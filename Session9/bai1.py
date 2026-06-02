# Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Bước 1: Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")
# → ["GE001", "GE002", "GE003-CANCEL", "GE004"]

# Bước 2: Chèn đơn hàng hỏa tốc GE000 vào đầu danh sách
delivery_orders.insert(0, "GE000")
# → ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"]
# Lưu ý: sau bước này, "GE002" đã dịch sang index 2

# Bước 3: Sửa mã đơn hàng GE002 thành GE002-UPDATED (dùng index 2)
delivery_orders[2] = "GE002-UPDATED"
# → ["GE000", "GE001", "GE002-UPDATED", "GE003-CANCEL", "GE004"]

# Bước 4: Xóa đơn hàng bị khách hủy (xóa theo GIÁ TRỊ, không phải index)
delivery_orders.remove("GE003-CANCEL")
# → ["GE000", "GE001", "GE002-UPDATED", "GE004"]

# Bước 5: Lấy đơn hàng cuối ra để bàn giao, LƯU KẾT QUẢ vào biến
transferred_order = delivery_orders.pop()
# → delivery_orders = ["GE000", "GE001", "GE002-UPDATED"]
# → transferred_order = "GE004"

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)