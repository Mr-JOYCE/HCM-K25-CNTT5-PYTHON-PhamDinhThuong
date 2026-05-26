print("===== TECHCORP HR KIOSK SYSTEM =====")
print("Hệ thống cập nhật hồ sơ & đánh giá năng lực\n")

while True:

    print("\n===== NHẬP THÔNG TIN NHÂN VIÊN =====")

    while True:

        employee_id = input(
            "Nhập mã nhân viên (Ví dụ: NV001): "
        ).strip()

        if employee_id != "":
            break

        print("[LỖI] Mã nhân viên không được để trống!")

    while True:

        full_name = input(
            "Nhập họ và tên: "
        ).strip()

        if full_name != "":
            break

        print("[LỖI] Họ tên không được để trống!")

    while True:

        department = input(
            "Nhập phòng ban (IT/HR/Marketing...): "
        ).strip()

        if department != "":
            break

        print("[LỖI] Phòng ban không được để trống!")

    while True:

        salary_input = input(
            "Nhập lương cơ bản VNĐ (>0): "
        )

        try:
            base_salary = float(salary_input)

            if base_salary > 0:
                break

            print("[LỖI] Lương phải lớn hơn 0!")

        except:
            print("[LỖI] Vui lòng nhập số hợp lệ!")

    while True:

        kpi_input = input(
            "Nhập điểm KPI (1.0 - 5.0): "
        )

        try:
            kpi_score = float(kpi_input)

            if 1.0 <= kpi_score <= 5.0:
                break

            print("[LỖI] KPI phải từ 1.0 đến 5.0!")

        except:
            print("[LỖI] KPI phải là số!")

    while True:

        working_days_input = input(
            "Nhập số ngày công (0 - 31): "
        )

        if working_days_input.isdigit():

            working_days = int(working_days_input)

            if 0 <= working_days <= 31:
                break

        print("[LỖI] Ngày công phải từ 0 đến 31!")

    print("\n===================================")
    print("     HỒ SƠ NHÂN SỰ ĐIỆN TỬ")
    print("===================================")

    print(f"Mã nhân viên : {employee_id}")
    print(f"Họ và tên    : {full_name}")
    print(f"Phòng ban    : {department}")
    print(f"Lương cơ bản : {base_salary:,.0f} VNĐ")
    print(f"Điểm KPI     : {kpi_score}")
    print(f"Ngày công    : {working_days}")

    print("===================================")

    print("\n===== SYSTEM LOG =====")

    print(f"employee_id  = {employee_id} | {type(employee_id)}")
    print(f"full_name    = {full_name} | {type(full_name)}")
    print(f"department   = {department} | {type(department)}")
    print(f"base_salary  = {base_salary} | {type(base_salary)}")
    print(f"kpi_score    = {kpi_score} | {type(kpi_score)}")
    print(f"working_days = {working_days} | {type(working_days)}")

    print("========================")

    while True:

        continue_program = input(
            "\nTiếp tục nhập nhân viên khác? (y/n): "
        ).lower()

        if continue_program in ["y", "n"]:
            break

        print("[LỖI] Chỉ được nhập y hoặc n!")

    if continue_program == "n":

        print("\nĐã thoát hệ thống HR Kiosk.")
        break