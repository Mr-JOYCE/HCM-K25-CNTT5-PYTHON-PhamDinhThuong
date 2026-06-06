# PHẦN 1: PHÂN TÍCH THIẾT KẾ HÀM
#
# --- Tên hàm: calculate_average(student) ---
# Input (Tham số): student - dict chứa math, physics, chemistry
# Output (Trả về): float - điểm trung bình 3 môn
# Pseudocode:
#   RETURN (student["math"] + student["physics"] + student["chemistry"]) / 3
#
# --- Tên hàm: get_academic_rank(average_score) ---
# Input (Tham số): average_score - float
# Output (Trả về): str - "Giỏi" | "Khá" | "Trung bình" | "Yếu"
# Pseudocode:
#   IF average >= 8.0: RETURN "Giỏi"
#   ELIF average >= 6.5: RETURN "Khá"
#   ELIF average >= 5.0: RETURN "Trung bình"
#   ELSE: RETURN "Yếu"
#
# --- Tên hàm: find_student_by_id(records, student_id) ---
# Input (Tham số): records - list[dict], student_id - str (đã chuẩn hóa)
# Output (Trả về): dict | None - sinh viên tìm thấy hoặc None
# Pseudocode:
#   FOR student IN records:
#       IF student["student_id"] == student_id: RETURN student
#   RETURN None
#
# --- Tên hàm: validate_score(score_input) ---
# Input (Tham số): score_input - str
# Output (Trả về): bool - True nếu hợp lệ (float 0-10), False nếu không
# Pseudocode:
#   TRY chuyển score_input sang float
#   IF 0 <= score <= 10: RETURN True
#   ELSE in lỗi và RETURN False
#   EXCEPT ValueError: in lỗi và RETURN False
#
# --- Tên hàm: display_menu() ---
# Input (Tham số): Không
# Output (Trả về): None (in menu ra màn hình)
# Pseudocode:
#   IN tiêu đề và 5 lựa chọn chức năng
#
# --- Tên hàm: display_grades(records) ---
# Input (Tham số): records - list[dict]
# Output (Trả về): None (in bảng điểm)
# Pseudocode:
#   IF records rỗng: in "Hệ thống chưa có dữ liệu sinh viên." và RETURN
#   IN tiêu đề bảng điểm
#   FOR từng student (có STT):
#       average = calculate_average(student)
#       rank = get_academic_rank(average)
#       IN dòng điểm từng môn, ĐTB (2 chữ số thập phân) và xếp loại
#   IN đường kẻ kết thúc
#
# --- Tên hàm: update_student_score(records) ---
# Input (Tham số): records - list[dict]
# Output (Trả về): None
# Pseudocode:
#   NHẬP mã SV, chuẩn hóa .strip().upper()
#   student = find_student_by_id(records, mã)
#   IF student is None: in lỗi không tìm thấy và RETURN
#   NHẬP môn (1-Toán, 2-Lý, 3-Hóa)
#   LẶP nhập điểm mới cho đến khi validate_score hợp lệ
#   CẬP NHẬT điểm môn tương ứng trong student
#   IN thông báo cập nhật thành công
#
# --- Tên hàm: generate_report(records) ---
# Input (Tham số): records - list[dict]
# Output (Trả về): None (in báo cáo thống kê)
# Pseudocode:
#   IF records rỗng: in "Hệ thống chưa có dữ liệu sinh viên." và RETURN
#   passed = 0, failed = 0
#   FOR student IN records:
#       IF calculate_average(student) >= 5.0: passed += 1
#       ELSE: failed += 1
#   Tính tỷ lệ % (2 chữ số thập phân), in báo cáo
#
# --- Tên hàm: find_valedictorian(records) ---
# Input (Tham số): records - list[dict]
# Output (Trả về): None (in vinh danh thủ khoa)
# Pseudocode:
#   IF records rỗng: in "Hệ thống chưa có dữ liệu sinh viên." và RETURN
#   Tìm student có calculate_average cao nhất
#   IN thông tin thủ khoa và lời chúc mừng
#
# --- Tên hàm: main() ---
# Input (Tham số): Không
# Output (Trả về): None
# Pseudocode:
#   WHILE True:
#       display_menu()
#       NHẬP lựa chọn 1-5
#       GỌI hàm tương ứng hoặc thoát / báo lỗi lựa chọn
# =============================================================================

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0,
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0,
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5,
    },
]

SUBJECT_MAP = {
    "1": ("math", "Toán"),
    "2": ("physics", "Lý"),
    "3": ("chemistry", "Hóa"),
}


def calculate_average(student):
    """Tính điểm trung bình 3 môn Toán, Lý, Hóa của một sinh viên."""
    return (student["math"] + student["physics"] + student["chemistry"]) / 3


def get_academic_rank(average_score):
    """Phân loại học lực theo điểm trung bình."""
    if average_score >= 8.0:
        return "Giỏi"
    if average_score >= 6.5:
        return "Khá"
    if average_score >= 5.0:
        return "Trung bình"
    return "Yếu"


def find_student_by_id(records, student_id):
    """Tìm sinh viên theo mã trong danh sách. Trả về dict hoặc None."""
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None


def validate_score(score_input):
    """Kiểm tra điểm có phải số float từ 0 đến 10 hay không."""
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
    except ValueError:
        pass

    print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
    return False


def display_menu():
    """Hiển thị menu chính của hệ thống."""
    print("===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")


def display_grades(records):
    """In bảng điểm và học lực của toàn bộ sinh viên."""
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- BẢNG ĐIỂM SINH VIÊN ---")
    for index, student in enumerate(records, start=1):
        average = calculate_average(student)
        rank = get_academic_rank(average)
        print(
            f"{index}. [{student['student_id']}] {student['name']:<15} | "
            f"Toán: {student['math']} | Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | ĐTB: {average:.2f} - {rank}"
        )
    print("---------------------------")


def update_student_score(records):
    """Cập nhật điểm một môn học cho sinh viên theo mã."""
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(records, student_id)

    if student is None:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return

    while True:
        subject_choice = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ").strip()
        if subject_choice in SUBJECT_MAP:
            field_name, subject_label = SUBJECT_MAP[subject_choice]
            break
        print("Lựa chọn môn học không hợp lệ, vui lòng nhập 1, 2 hoặc 3!")

    while True:
        score_input = input("Nhập điểm mới: ").strip()
        if validate_score(score_input):
            new_score = float(score_input)
            break

    student[field_name] = new_score
    print(
        f">> Đã cập nhật điểm {subject_label} của sinh viên "
        f"'{student['name']}' thành {new_score}."
    )


def generate_report(records):
    """Thống kê số sinh viên qua môn và trượt môn theo ĐTB."""
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    passed = sum(1 for student in records if calculate_average(student) >= 5.0)
    failed = total - passed

    passed_percent = (passed / total) * 100
    failed_percent = (failed / total) * 100

    print("--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): {passed} sinh viên "
        f"(Chiếm {passed_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): {failed} sinh viên "
        f"(Chiếm {failed_percent:.2f}%)"
    )
    print("----------------------")


def find_valedictorian(records):
    """Tìm và vinh danh sinh viên có điểm trung bình cao nhất."""
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = max(records, key=calculate_average)
    top_average = calculate_average(top_student)

    print("--- VINH DANH THỦ KHOA ---")
    print(f" Sinh viên: {top_student['name']} (Mã: {top_student['student_id']})")
    print(f" Điểm Trung Bình: {top_average:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")


def main():
    """Vòng lặp menu chính điều hướng các chức năng nghiệp vụ."""
    while True:
        print()
        display_menu()
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_grades(student_records)
        elif choice == "2":
            update_student_score(student_records)
        elif choice == "3":
            generate_report(student_records)
        elif choice == "4":
            find_valedictorian(student_records)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    main()
