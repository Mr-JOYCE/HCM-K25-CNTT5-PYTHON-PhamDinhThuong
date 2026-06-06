# PHẦN 1: PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
#
# --- Tại sao tách thành nhiều hàm nhỏ thay vì một vòng lặp while dài? ---
# - Dễ đọc, dễ bảo trì: mỗi hàm đảm nhận một nhiệm vụ rõ ràng.
# - Dễ kiểm thử: có thể kiểm tra từng hàm (validate_score, get_rank...) độc lập.
# - Tái sử dụng: validate_score dùng chung cho thêm mới và cập nhật điểm.
# - Giảm lỗi: logic tách biệt, sửa một chức năng không ảnh hưởng phần còn lại.
#
# --- Phân tích Input/Output từng hàm ---
#
# display_menu()
#   Input : Không
#   Output: None (in menu ra màn hình)
#
# display_students(student_list)
#   Input : list[dict] - danh sách học viên
#   Output: None (in danh sách hoặc thông báo trống)
#
# validate_score(score_input)
#   Input : str - chuỗi người dùng nhập
#   Output: bool - True nếu là số từ 0 đến 10, False nếu không hợp lệ
#
# find_student_by_id(student_list, student_id)
#   Input : list[dict], str - danh sách và mã học viên (đã chuẩn hóa)
#   Output: dict | None - học viên tìm thấy, hoặc None nếu không có
#
# input_non_empty(prompt)
#   Input : str - câu nhắc nhập liệu
#   Output: str - giá trị đã strip, không rỗng
#
# input_valid_score(prompt)
#   Input : str - câu nhắc nhập điểm
#   Output: float - điểm hợp lệ (0-10), gọi validate_score để kiểm tra
#
# add_student(student_list)
#   Input : list[dict] - danh sách (tham chiếu, thêm phần tử trực tiếp)
#   Output: None
#
# update_score(student_list)
#   Input : list[dict]
#   Output: None
#
# calculate_average(math_score, english_score)
#   Input : float, float - điểm Toán và Anh
#   Output: float - điểm trung bình
#
# get_rank(average_score)
#   Input : float - điểm trung bình
#   Output: str - "Giỏi" | "Khá" | "Trung bình" | "Yếu"
#
# evaluate_students(student_list)
#   Input : list[dict]
#   Output: None (in bảng đánh giá học lực)
#
# main()
#   Input : Không
#   Output: None - vòng lặp menu chính
# =============================================================================

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0,
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5,
    },
]


def display_menu():
    """Hiển thị menu chính của hệ thống quản lý điểm thi."""
    print("===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")


def display_students(student_list):
    """
    In danh sách học viên kèm mã, tên và điểm Toán/Anh.
    Nếu danh sách rỗng, thông báo không có dữ liệu.
    """
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return

    for index, student in enumerate(student_list, start=1):
        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']:<15} | "
            f"Toán: {student['math_score']} | "
            f"Anh: {student['english_score']}"
        )


def validate_score(score_input):
    """
    Kiểm tra điểm có phải số từ 0 đến 10 hay không.
    Trả về True nếu hợp lệ, False nếu không.
    """
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
    except ValueError:
        pass

    print("Điểm không hợp lệ, phải là số từ 0 đến 10")
    return False


def find_student_by_id(student_list, student_id):
    """
    Tìm học viên theo mã trong danh sách.
    Trả về dictionary học viên nếu tìm thấy, None nếu không.
    """
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None


def input_non_empty(prompt):
    """
    Yêu cầu người dùng nhập giá trị không rỗng (sau khi strip).
    Trả về chuỗi đã loại bỏ khoảng trắng hai đầu.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Tên không được để trống, vui lòng nhập lại!")


def input_valid_score(prompt):
    """
    Yêu cầu nhập điểm hợp lệ, tái sử dụng validate_score.
    Trả về điểm dạng float.
    """
    while True:
        score_input = input(prompt).strip()
        if validate_score(score_input):
            return float(score_input)


def add_student(student_list):
    """
    Thêm học viên mới vào danh sách sau khi kiểm tra mã trùng và điểm hợp lệ.
    Chuẩn hóa mã (viết hoa) và tên (title case).
    """
    while True:
        student_id = input("Mã Học Viên: ").strip().upper()
        if not student_id:
            print("Mã học viên không được để trống, vui lòng nhập lại!")
            continue
        if find_student_by_id(student_list, student_id) is not None:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
            continue
        break

    name = input_non_empty("Tên Học viên: ").title()

    math_score = input_valid_score("Nhập Điểm Toán: ")
    english_score = input_valid_score("Nhập Điểm Anh: ")

    student_list.append(
        {
            "student_id": student_id,
            "name": name,
            "math_score": math_score,
            "english_score": english_score,
        }
    )
    print("Thêm học viên thành công!")


def update_score(student_list):
    """
    Cập nhật điểm Toán và Anh cho học viên theo mã.
    Dùng find_student_by_id để tra cứu và validate_score để kiểm tra điểm mới.
    """
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(student_list, student_id)

    if student is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    student["math_score"] = input_valid_score("Nhập điểm Toán mới: ")
    student["english_score"] = input_valid_score("Nhập điểm Anh mới: ")
    print("Cập nhật điểm thành công!")


def calculate_average(math_score, english_score):
    """Tính điểm trung bình từ điểm Toán và điểm Anh."""
    return (math_score + english_score) / 2


def get_rank(average_score):
    """
    Xếp loại học lực theo điểm trung bình.
    >= 8.0: Giỏi | >= 6.5: Khá | >= 5.0: Trung bình | < 5.0: Yếu
    """
    if average_score >= 8.0:
        return "Giỏi"
    if average_score >= 6.5:
        return "Khá"
    if average_score >= 5.0:
        return "Trung bình"
    return "Yếu"


def evaluate_students(student_list):
    """
    Đánh giá học lực toàn bộ học viên: in ĐTB và xếp loại.
    """
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return

    for student in student_list:
        average = calculate_average(student["math_score"], student["english_score"])
        rank = get_rank(average)
        print(
            f"Mã: {student['student_id']} | Tên: {student['name']} | "
            f"ĐTB: {average:.2f} | Xếp loại: {rank}"
        )


def main():
    """Vòng lặp menu chính: điều hướng tới từng chức năng nghiệp vụ."""
    while True:
        print()
        display_menu()
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            print("\n*** Chức năng 1: Hiển thị danh sách học viên\n")
            display_students(students)
        elif choice == "2":
            print("\n*** Chức năng 2: Thêm học viên mới\n")
            add_student(students)
        elif choice == "3":
            print("\n*** Chức năng 3: Cập nhật điểm thi theo mã học viên\n")
            update_score(students)
        elif choice == "4":
            print("\n*** Chức năng 4: Đánh giá học lực\n")
            evaluate_students(students)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    main()
