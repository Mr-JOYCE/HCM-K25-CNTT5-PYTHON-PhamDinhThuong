branch_names = [
    "Highlands Nhà Thờ",
    "Highlands Bà Triệu",
    "Highlands Nguyễn Du",
    "Highlands Landmark 81",
    "Highlands Trần Hưng Đạo",
]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]


def format_status(achieved):
    return "Đạt" if achieved else "Không Đạt"


def display_report():
    print("Danh sách báo cáo doanh thu Highlands Coffee:")
    print("{:<4} {:<25} {:>15} {:>15}".format("STT", "Chi nhánh", "Doanh thu", "Trạng thái"))
    print("=" * 63)

    for index in range(len(branch_names)):
        name = branch_names[index]
        revenue = daily_revenues[index]
        status = format_status(target_achieved[index])
        print("{:<4} {:<25} {:>15,} {:>15}".format(index + 1, name, revenue, status))

    total_revenue = sum(daily_revenues)
    print("=" * 63)
    print(f"Tổng doanh thu toàn hệ thống: {total_revenue:,} VNĐ")


def display_high_low():
    highest = max(daily_revenues)
    lowest = min(daily_revenues)
    highest_index = daily_revenues.index(highest)
    lowest_index = daily_revenues.index(lowest)

    print("Thống kê chi nhánh doanh thu cao nhất và thấp nhất:")
    print(f"- Chi nhánh doanh thu cao nhất: {branch_names[highest_index]} ({highest:,} VNĐ)")
    print(f"- Chi nhánh doanh thu thấp nhất: {branch_names[lowest_index]} ({lowest:,} VNĐ)")


def filter_failed_branches():
    failed_branches = []
    for index in range(len(branch_names)):
        if not target_achieved[index]:
            failed_branches.append(branch_names[index])

    print("Danh sách chi nhánh không đạt chỉ tiêu:")
    print(failed_branches)


def main():
    while True:
        print("===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
        print("1. Hiển thị báo cáo doanh thu tổng hợp")
        print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
        print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
        print("4. Thoát chương trình")
        print("================================================")
        choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

        if choice == "1":
            display_report()
        elif choice == "2":
            display_high_low()
        elif choice == "3":
            filter_failed_branches()
        elif choice == "4":
            print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
            break
        else:
            print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")

        print()


if __name__ == "__main__":
    main()
