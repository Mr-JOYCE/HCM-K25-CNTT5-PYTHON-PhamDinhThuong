print("=== HỆ THỐNG TIẾP NHẬN SINH HIỆU ===")

patient_code = input("Nhập mã bệnh nhân: ")

temperature_input = input("Nhập nhiệt độ cơ thể: ")
heart_rate_input = input("Nhập nhịp tim: ")

temperature = float(temperature_input)
heart_rate = int(heart_rate_input)

print("\n=== KẾT QUẢ CHUẨN HÓA DỮ LIỆU ===")

print("Mã bệnh nhân:", patient_code)

print("Nhiệt độ cơ thể:", temperature, "độ C")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(temperature))

print("Nhịp tim:", heart_rate, "nhịp/phút")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))

print("--------------------------------------")
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")