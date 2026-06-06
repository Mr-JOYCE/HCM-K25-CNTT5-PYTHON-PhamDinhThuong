# PHẦN 1: PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
#
# --- Modular Design: find_student(records, student_id) ---
# Thay vì lặp lại vòng for tìm kiếm ở 4 chức năng, tách thành một hàm duy nhất.
# Lợi ích: giảm trùng lặp code, sửa logic tìm kiếm một chỗ, dễ kiểm thử độc lập.
#
# --- Phân tích Input/Output ---
#
# find_student(records, student_id)
#   Input : list[dict], str (mã đã chuẩn hóa)
#   Output: int - index trong list, hoặc -1 nếu không tìm thấy
#
# get_member_status(current_points)
#   Input : int
#   Output: str - trạng thái thành viên theo ngưỡng điểm
#
# validate_positive_integer(value_input)
#   Input : str
#   Output: tuple(bool, int|None) - True và giá trị nếu hợp lệ
#
# validate_multiplier(value_input)
#   Input : str
#   Output: tuple(bool, float|None) - True nếu float từ 1.0 đến 3.0
#
# display_menu()
#   Input : Không | Output: None (in menu)
#
# display_statements(records)
#   Input : list[dict] | Output: None (in sao kê, không đổi dữ liệu)
#
# redeem_rewards(records)
#   Input : list[dict] | Output: None
#   Luồng dữ liệu: current_points -= amount, spent_points += amount
#
# appeal_score(records)
#   Input : list[dict] | Output: None
#   Luồng dữ liệu: spent_points -= amount, current_points += amount,
#                   refunded_points += amount
#
# activate_multiplier(records)
#   Input : list[dict] | Output: None
#   Luồng dữ liệu: multiplier = hệ số mới
#
# grade_assignment(records)
#   Input : list[dict] | Output: None
#   Luồng dữ liệu: current_points += base_score * multiplier
#
# main()
#   Input : Không | Output: None (vòng lặp menu)
#
# --- Pseudocode: redeem_rewards (Chức năng 2) ---
#   student_id = chuẩn hóa(input mã)
#   index = find_student(records, student_id)
#   IF index == -1: báo lỗi và RETURN
#   LẶP nhập số điểm tiêu:
#       IF không phải số nguyên dương: báo lỗi, nhập lại
#       IF amount > current_points: báo "Số dư điểm không đủ..." và RETURN
#   student.current_points -= amount
#   student.spent_points += amount
#   in thông báo giao dịch thành công
#
# --- Pseudocode: grade_assignment (Chức năng 5) ---
#   student_id = chuẩn hóa(input mã)
#   index = find_student(records, student_id)
#   IF index == -1: báo lỗi và RETURN
#   LẶP nhập điểm gốc:
#       IF không phải số nguyên dương: báo lỗi, nhập lại
#   actual_points = base_score * student.multiplier
#   student.current_points += actual_points
#   in hệ số, điểm thực nhận và thông báo cộng điểm
# =============================================================================

student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0,
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5,
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0,
    },
]


def find_student(records, student_id):
    """
    Tìm index của học viên theo mã trong danh sách.
    Trả về index nếu tìm thấy, -1 nếu không.
    """
    for index, student in enumerate(records):
        if student["student_id"] == student_id:
            return index
    return -1


def get_member_status(current_points):
    """Xác định trạng thái thành viên dựa trên điểm hiện có."""
    if current_points < 500:
        return "Cần tích lũy thêm"
    if current_points <= 1500:
        return "Thành viên tiềm năng"
    return "Thành viên ưu tú"


def format_multiplier(multiplier):
    """Định dạng hệ số nhân dạng x1.0, x1.5, x2.5..."""
    if multiplier == int(multiplier):
        return f"x{multiplier:.1f}"
    return f"x{multiplier}"


def format_points(points):
    """Hiển thị điểm dạng số nguyên nếu không có phần thập phân."""
    if points == int(points):
        return str(int(points))
    return str(points)


def validate_positive_integer(value_input):
    """
    Kiểm tra giá trị nhập có phải số nguyên dương hay không.
    Trả về (True, value) nếu hợp lệ, (False, None) nếu không.
    """
    try:
        value = int(value_input)
        if value > 0:
            return True, value
    except ValueError:
        pass

    print("Vui lòng nhập số nguyên dương!")
    return False, None


def validate_multiplier(value_input):
    """
    Kiểm tra hệ số nhân có phải float từ 1.0 đến 3.0 hay không.
    Trả về (True, value) nếu hợp lệ, (False, None) nếu không.
    """
    try:
        value = float(value_input)
        if 1.0 <= value <= 3.0:
            return True, value
    except ValueError:
        pass

    print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0")
    return False, None


def normalize_student_id(raw_id):
    """Chuẩn hóa mã học viên: xóa khoảng trắng và viết hoa."""
    return raw_id.strip().upper()


def display_menu():
    """Hiển thị menu chính của hệ thống ngân hàng điểm số."""
    print("===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
    print("1. Hiển thị sao kê điểm số")
    print("2. Đổi điểm lấy phần thưởng")
    print("3. Phúc khảo bài thi (Hoàn điểm)")
    print("4. Kích hoạt (Hệ số nhân điểm)")
    print("5. Chấm bài (thêm điểm)")
    print("6. Thoát chương trình")
    print("=====================================================")


def display_statements(records):
    """In sao kê điểm số và trạng thái của toàn bộ học viên."""
    print("--- SAO KÊ ĐIỂM SỐ ---")
    if not records:
        print("Hệ thống chưa có dữ liệu học viên.")
        print("----------------------")
        return

    for index, student in enumerate(records, start=1):
        status = get_member_status(student["current_points"])
        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']:<16} | "
            f"Hiện có: {student['current_points']:<4} | "
            f"Đã tiêu: {student['spent_points']:<4} | "
            f"Hoàn trả: {student['refunded_points']:<3} | "
            f"Hệ số: {format_multiplier(student['multiplier']):<4} | "
            f"Trạng thái: {status}"
        )
    print("----------------------")


def redeem_rewards(records):
    """Xử lý đổi điểm lấy phần thưởng: trừ current_points, cộng spent_points."""
    student_id = normalize_student_id(input("Nhập mã học viên đổi quà: "))
    index = find_student(records, student_id)

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    student = records[index]

    while True:
        is_valid, amount = validate_positive_integer(
            input("Nhập số điểm cần tiêu: ").strip()
        )
        if not is_valid:
            continue
        if amount > student["current_points"]:
            print("Số dư điểm không đủ để thực hiện giao dịch!")
            return
        break

    student["current_points"] -= amount
    student["spent_points"] += amount
    print(
        f">> Giao dịch thành công! '{student['name']}' đã tiêu {amount} điểm. "
        f"Số dư còn lại: {student['current_points']} điểm."
    )


def appeal_score(records):
    """Hoàn điểm phúc khảo: giảm spent_points, tăng current và refunded_points."""
    student_id = normalize_student_id(input("Nhập mã học viên cần phúc khảo: "))
    index = find_student(records, student_id)

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    student = records[index]

    while True:
        is_valid, amount = validate_positive_integer(
            input("Nhập số điểm hoàn lại: ").strip()
        )
        if not is_valid:
            continue
        if amount > student["spent_points"]:
            print("Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu!")
            return
        break

    student["spent_points"] -= amount
    student["current_points"] += amount
    student["refunded_points"] += amount
    print(f">> Hoàn điểm thành công! '{student['name']}' được cộng lại {amount} điểm.")


def activate_multiplier(records):
    """Kích hoạt hệ số nhân điểm mới cho học viên trong dịp lễ."""
    student_id = normalize_student_id(input("Nhập mã học viên nhận hệ số: "))
    index = find_student(records, student_id)

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    student = records[index]

    while True:
        is_valid, multiplier = validate_multiplier(
            input("Nhập hệ số nhân mới (1.0 - 3.0): ").strip()
        )
        if is_valid:
            break

    student["multiplier"] = multiplier
    print(
        f">> Đã kích hoạt hệ số {format_multiplier(multiplier)} "
        f"cho học viên '{student['name']}'."
    )


def grade_assignment(records):
    """Chấm bài và cộng điểm thực nhận (điểm gốc * hệ số) vào tài khoản."""
    student_id = normalize_student_id(input("Nhập mã học viên vừa nộp bài: "))
    index = find_student(records, student_id)

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    student = records[index]

    while True:
        is_valid, base_score = validate_positive_integer(
            input("Nhập số điểm gốc đạt được: ").strip()
        )
        if is_valid:
            break

    actual_points = base_score * student["multiplier"]
    student["current_points"] += actual_points

    print(
        f">> Hệ số hiện tại của '{student['name']}' là "
        f"{format_multiplier(student['multiplier'])}. "
        f"Điểm thực nhận: {format_points(actual_points)}."
    )
    print(f">> Đã cộng {format_points(actual_points)} điểm vào tài khoản!")


def main():
    """Vòng lặp menu chính điều hướng các chức năng nghiệp vụ."""
    while True:
        print()
        display_menu()
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            display_statements(student_records)
        elif choice == "2":
            redeem_rewards(student_records)
        elif choice == "3":
            appeal_score(student_records)
        elif choice == "4":
            activate_multiplier(student_records)
        elif choice == "5":
            grade_assignment(student_records)
        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    main()
