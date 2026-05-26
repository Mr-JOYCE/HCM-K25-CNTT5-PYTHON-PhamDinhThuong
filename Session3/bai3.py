print("===== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ =====")

for employee_number in range(1, 4):

    print(f"\n----- Nhân viên số {employee_number} -----")

    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")

    if employee_id.strip() == "" or full_name.strip() == "":

        print("\n[CẢNH BÁO]")
        print("Mã nhân viên hoặc Họ tên không hợp lệ!")
        print("Không thể tạo hồ sơ nhân sự.")

        continue

    print("\n==============================")
    print("PHIẾU HỒ SƠ NHÂN SỰ ĐIỆN TỬ")
    print("==============================")
    print(f"Mã nhân viên : {employee_id}")
    print(f"Họ và tên    : {full_name}")
    print(f"Phòng ban    : {department}")
    print("==============================")

# Kết thúc chương trình
print("\nĐã hoàn tất onboarding cho 3 nhân viên!")