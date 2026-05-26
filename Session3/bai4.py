print("===== HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI =====")

while True:

    user_input = input(
        "Vui lòng nhập số lượng nhân sự mới trong tháng này: "
    )

    if not user_input.lstrip("-").isdigit():

        print("\n[LỖI] Vui lòng nhập một số nguyên hợp lệ!\n")
        continue

    employee_count = int(user_input)

    if employee_count <= 0:

        print("\n[LỖI] Số lượng nhân sự phải lớn hơn 0!")
        print("Vui lòng nhập lại.\n")

        continue

    print(f"\nGhi nhận thành công {employee_count} nhân sự mới.")
    break