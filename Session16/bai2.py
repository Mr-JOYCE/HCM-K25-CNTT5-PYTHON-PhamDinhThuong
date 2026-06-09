# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription: list):
    # Lập trình viên cố gắng sao chép đơn thuốc sang ngày mới
    new_prescription = old_prescription.copy()
    # Cố gắng đổi tên thuốc ở vị trí đầu tiên (index 0) từ Panadol thành Paracetamol
    new_prescription[0] = "Paracetamol"
    # Thêm thuốc mới cho ngày hôm nay
    new_prescription.append("Oresol")
    return new_prescription
    
# Hệ thống chạy cấp thuốc cho ngày hôm nay
today_prescription = update_prescription(yesterday_prescription)
print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)


