import random

ten = input("Nhập tên bệnh nhân: ")
gioi_tinh = input("Nhập giới tính: ")

nam_sinh = int(input("Nhập năm sinh: "))

dien_thoai = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
trieu_chung = input("Nhập triệu chứng ban đầu: ")

chi_phi = float(input("Nhập chi phí khám: "))

so_ngau_nhien = random.randint(100, 999)

ma_benh_nhan = "BN" + str(nam_sinh) + str(so_ngau_nhien)

print("\n--- THẺ BỆNH NHÂN ---")

print("Mã BN      :", ma_benh_nhan)

print("\nTên        :", ten)
print("Giới tính  :", gioi_tinh)
print("Năm sinh   :", nam_sinh)
print("Điện thoại :", dien_thoai)
print("Email      :", email)
print("Triệu chứng:", trieu_chung)
print("Chi phí    :", chi_phi, "VND")