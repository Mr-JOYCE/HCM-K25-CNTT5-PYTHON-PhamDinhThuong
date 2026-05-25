print("===================================================")
print("     KIOSK TIẾP NHẬN & KHAI BÁO Y TẾ")
print("        BỆNH VIỆN SỨC KHỎE VÀNG")
print("===================================================")

print("\nXin vui lòng nhập đầy đủ thông tin bên dưới.")
print("Hệ thống có ví dụ minh họa để hỗ trợ nhập liệu.\n")

patient_name = input(
    "Nhập họ tên bệnh nhân (Ví dụ: Nguyễn Văn A): "
)

patient_code = input(
    "Nhập mã bệnh nhân (Ví dụ: BN1001): "
)

patient_age_input = input(
    "Nhập tuổi bệnh nhân bằng số (Ví dụ: 25): "
)

body_temperature_input = input(
    "Nhập nhiệt độ cơ thể dạng số thực (Ví dụ: 37.5): "
)

heart_rate_input = input(
    "Nhập nhịp tim dạng số nguyên (Ví dụ: 85): "
)

body_weight_input = input(
    "Nhập cân nặng dạng số thực kg (Ví dụ: 65.5): "
)

patient_age = int(patient_age_input)

body_temperature = float(body_temperature_input)

heart_rate = int(heart_rate_input)

body_weight = float(body_weight_input)

print("\n")
print("===================================================")
print("           PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("===================================================")

print(f"Họ tên bệnh nhân : {patient_name}")
print(f"Mã bệnh nhân     : {patient_code}")
print(f"Tuổi              : {patient_age}")

print("-----------------------------------------------")

print(f"Nhiệt độ cơ thể  : {body_temperature} °C")
print(f"Nhịp tim         : {heart_rate} nhịp/phút")
print(f"Cân nặng         : {body_weight} kg")

print("===================================================")

print("\n")
print("===================================================")
print("              SYSTEM LOG FOR IT")
print("===================================================")

print("patient_name      =", patient_name,
      "-", type(patient_name))

print("patient_code      =", patient_code,
      "-", type(patient_code))

print("patient_age       =", patient_age,
      "-", type(patient_age))

print("body_temperature  =", body_temperature,
      "-", type(body_temperature))

print("heart_rate        =", heart_rate,
      "-", type(heart_rate))

print("body_weight       =", body_weight,
      "-", type(body_weight))

print("===================================================")

print("\nThông báo:")
print("Dữ liệu đã được chuẩn hóa thành công.")
print("Hệ thống Monitor và Hồ sơ điện tử đã sẵn sàng.")