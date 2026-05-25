print("=== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ===")

full_name = input("Nhập họ tên bệnh nhân: ")
medical_code = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám: ")

print("\n=== PHIẾU KHÁM BỆNH ĐIỆN TỬ ===")

print(
    "Bệnh nhân:",
    full_name,
    "- Mã BA:",
    medical_code,
    "- Chuyển tới:",
    department
)