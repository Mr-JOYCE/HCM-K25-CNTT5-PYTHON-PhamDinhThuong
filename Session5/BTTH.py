"""
Bài tập tổng hợp: Vòng lặp nâng cao
Chương trình quản lý số ngày làm việc nhân viên trong tháng.

Input/Output:
- Input:
  + Số lượng nhân viên cần kiểm tra (số nguyên dương)
  + Tên nhân viên (chuỗi)
  + Số ngày làm việc trong tháng (số nguyên từ 0 tới 22)
- Output:
  + Thông báo nếu dữ liệu không hợp lệ
  + Thông báo nhân viên nghỉ toàn bộ tháng nếu số ngày là 0
  + Biểu đồ số ngày làm việc bằng dấu *
  + Thống kê mức độ làm việc: "Làm việc chăm chỉ" hoặc "Làm việc bình thường"

Thuật toán:
1. Yêu cầu người dùng nhập số nhân viên. Nếu không hợp lệ, nhập lại.
2. Với mỗi nhân viên:
   a. Nhập tên nhân viên.
   b. Nhập số ngày làm việc.
   c. Nếu số ngày < 0 hoặc > 22, in thông báo và bỏ qua nhân viên đó (continue).
   d. Nếu số ngày == 0, in thông báo nghỉ toàn bộ tháng và tiếp tục sang nhân viên tiếp theo.
   e. Nếu hợp lệ, in biểu đồ bằng dấu *, dùng nested loop.
   f. In mức độ làm việc theo quy tắc:
      - >= 18: "Làm việc chăm chỉ"
      - 1..17: "Làm việc bình thường"
"""


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
                continue
            return value
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")


def print_working_day_chart(work_days):
    print("Biểu đồ ngày làm việc:")
    for row in range(1):
        for star_index in range(work_days):
            print("*", end="")
    print()


def main():
    print("=== QUẢN LÝ NGÀY LÀM VIỆC NHÂN VIÊN ===")
    employee_count = read_positive_int("Nhập số lượng nhân viên: ")

    for employee_index in range(1, employee_count + 1):
        print(f"\nNhập thông tin nhân viên thứ {employee_index}:")
        employee_name = input("Tên nhân viên: ").strip()

        if not employee_name:
            print("Tên nhân viên không được để trống. Bỏ qua nhân viên này.")
            continue

        work_days = read_int("Số ngày làm việc trong tháng (0-22): ")
        if work_days < 0 or work_days > 22:
            print("Dữ liệu không hợp lệ")
            continue

        if work_days == 0:
            print(f"{employee_name} nghỉ toàn bộ tháng")
            continue

        print_working_day_chart(work_days)

        if work_days >= 18:
            print(f"{employee_name}: Làm việc chăm chỉ")
        else:
            print(f"{employee_name}: Làm việc bình thường")


if __name__ == "__main__":
    main()
