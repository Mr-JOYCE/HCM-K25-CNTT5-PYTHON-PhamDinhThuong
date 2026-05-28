"""
Bài toán: Hệ thống quản lý thống kê học viên theo chi nhánh

Phân tích Input/Output:
- Input:
  + Lựa chọn menu: số nguyên 1-3
  + Số lượng chi nhánh: số nguyên dương
  + Số lớp của mỗi chi nhánh: số nguyên dương
  + Số học viên của từng lớp: số nguyên >= 0
- Output:
  + Báo cáo tổng số học viên theo từng chi nhánh
  + Chi nhánh có tổng số học viên cao nhất
  + Danh sách các lớp có sĩ số thấp (< 10 học viên) hoặc thông báo không có lớp như vậy
  + Hướng dẫn sử dụng
  + Thông báo thoát chương trình

Thiết kế giải pháp:
1. Hiển thị menu chính trong vòng lặp cho đến khi người dùng chọn Thoát.
2. Kiểm tra hợp lệ lựa chọn menu, nếu không hợp lệ thì yêu cầu nhập lại.
3. Khi chọn chức năng nhập dữ liệu:
   - Nhập số chi nhánh.
   - Với mỗi chi nhánh, nhập số lớp.
   - Với mỗi lớp, nhập số học viên và kiểm tra >= 0.
   - Cập nhật tổng học viên theo chi nhánh và danh sách lớp có sĩ số < 10.
   - In kết quả sau khi nhập xong.
4. Chức năng hiển thị hướng dẫn: giải thích cách nhập và quy tắc thống kê.
5. Chức năng thoát: thông báo và kết thúc vòng lặp.

Pseudocode:
- while True:
    show menu
    choice = read integer
    if choice == 1:
        collect branch data
        print report
    elif choice == 2:
        print instructions
    elif choice == 3:
        print exit message
        break
    else:
        print invalid selection

"""


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Giá trị không hợp lệ. Vui lòng nhập lại.")
                continue
            return value
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")


def read_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue
            return value
        except ValueError:
            print("Số học viên không hợp lệ. Vui lòng nhập lại.")


def show_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ THỐNG KÊ HỌC VIÊN THEO CHI NHÁNH =====")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Hiển thị hướng dẫn sử dụng")
    print("3. Thoát chương trình")


def show_instructions():
    print("\nHƯỚNG DẪN SỬ DỤNG:")
    print("- Chọn 1 để nhập số chi nhánh, số lớp mỗi chi nhánh và số học viên của từng lớp.")
    print("- Mỗi chi nhánh có thể có số lớp khác nhau.")
    print("- Số học viên phải là số nguyên không âm.")
    print("- Sau khi nhập xong, chương trình sẽ thống kê:")
    print("  + Tổng số học viên của từng chi nhánh")
    print("  + Chi nhánh có tổng số học viên cao nhất")
    print("  + Các lớp có sĩ số thấp (dưới 10 học viên)")
    print("- Chọn 3 để thoát chương trình.")


def process_attendance_data():
    branch_count = read_positive_int("Nhập số lượng chi nhánh: ")
    branch_totals = []
    low_capacity_classes = []

    for branch_index in range(1, branch_count + 1):
        print(f"\nChi nhánh {branch_index}:")
        class_count = read_positive_int(f"Nhập số lớp của chi nhánh {branch_index}: ")
        branch_total = 0

        for class_index in range(1, class_count + 1):
            attendance = read_non_negative_int(
                f"Nhập số học viên của lớp {class_index} tại chi nhánh {branch_index}: "
            )
            branch_total += attendance
            if attendance < 10:
                low_capacity_classes.append((branch_index, class_index, attendance))

        branch_totals.append(branch_total)
        print(f"Tổng học viên của chi nhánh {branch_index}: {branch_total}")

    max_total = max(branch_totals)
    max_branches = [i + 1 for i, total in enumerate(branch_totals) if total == max_total]
    if len(max_branches) == 1:
        print(f"\nChi nhánh có tổng số học viên cao nhất: Chi nhánh {max_branches[0]} ({max_total} học viên)")
    else:
        print(f"\nCác chi nhánh có tổng số học viên cao nhất ({max_total} học viên):")
        print(", ".join(str(branch) for branch in max_branches))

    if low_capacity_classes:
        print("\nDanh sách lớp có sĩ số thấp (dưới 10 học viên):")
        for branch_index, class_index, attendance in low_capacity_classes:
            print(f"- Chi nhánh {branch_index} - Lớp {class_index}: {attendance} học viên")
    else:
        print("\nKhông có lớp nào có sĩ số dưới 10 học viên.")


def main():
    while True:
        show_menu()
        choice = read_positive_int("Chọn chức năng (1-3): ")

        if choice == 1:
            process_attendance_data()
        elif choice == 2:
            show_instructions()
        elif choice == 3:
            print("\nThoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại chức năng từ 1 đến 3.")


if __name__ == "__main__":
    main()
