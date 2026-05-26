print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

for employee_number in range(1, 4):

    print(f"\n--- Đang xử lý nhân viên số {employee_number} ---")

    working_days = int(input("Nhập số ngày công trong tháng: "))

    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        print("------------------------------------------------")
        
        continue

    bonus_amount = working_days * 200000

    print(f"→ Đã gửi Email: Chúc mừng nhận được {bonus_amount} VNĐ tiền thưởng!")

    print("------------------------------------------------")

print("\nĐã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")