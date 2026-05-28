# PHÂN TÍCH LỖI:
# Chương trình đang duyệt vòng lặp ngoài theo tháng,
# sau đó mới duyệt theo chi nhánh.
#
# Điều này khiến dữ liệu được nhóm theo:
#   Tháng -> Chi nhánh
#
# Trong khi yêu cầu nghiệp vụ cần:
#   Chi nhánh -> Tháng
#
# Vì hệ thống báo cáo doanh thu cần gom dữ liệu
# theo từng chi nhánh để dễ theo dõi và tổng hợp.
#
# Do đó:
# - Vòng lặp ngoài phải duyệt theo chi nhánh
# - Vòng lặp trong phải duyệt theo tháng

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

result = ""

for branch in range(1, branch_count + 1):

    result += f"\n=== Chi nhánh {branch} ===\n"

    for month in range(1, month_count + 1):

        revenue = int(
            input(f"Nhập doanh thu chi nhánh {branch}, tháng {month}: ")
        )

        result += f"Tháng {month}: {revenue} triệu đồng\n"

print("\n===== BÁO CÁO DOANH THU =====")
print(result)