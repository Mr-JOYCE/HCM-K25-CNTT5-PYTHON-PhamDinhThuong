print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

total_budget = 0

for employee_number in range(1, 4):

    print(f"\nĐang xử lý nhân viên số {employee_number}")

    salary = int(input("Nhập mức lương (VNĐ): "))

    total_budget = total_budget + salary

print("\n=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")