grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
]


def display_menu():
    """Hiển thị menu chức năng của hệ thống."""
    print("=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===")
    print("1. Xem bảng điểm học sinh")
    print("2. Thêm hồ sơ học sinh mới")
    print("3. Cập nhật điểm số")
    print("4. Xóa hồ sơ học sinh")
    print("5. Thoát chương trình")
    print("================================")


def calculate_average(scores):
    """Tính điểm trung bình từ tuple (toán, anh)."""
    math_score, english_score = scores
    return (math_score + english_score) / 2


def find_student_index(book, student_id):
    """Tìm vị trí học sinh trong danh sách theo mã ID. Trả về index hoặc -1."""
    for index, student in enumerate(book):
        if student["id"] == student_id:
            return index
    return -1


def input_score(prompt):
    """Nhập điểm số hợp lệ dạng float."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Điểm không hợp lệ, vui lòng nhập số!")


def display_grades(book):
    """In bảng điểm học sinh kèm điểm trung bình."""
    print("--- BẢNG ĐIỂM HỌC SINH ---")
    print("Mã SV | Tên Học Sinh        | Điểm Toán | Điểm Anh | ĐTB")
    print("-----------------------------------------------------------------------")

    if not book:
        print("(Danh sách trống)")
    else:
        for student in book:
            math_score, english_score = student["info"]
            average = calculate_average(student["info"])
            print(
                f"{student['id']:<5} | {student['name']:<19} | "
                f"{math_score:<9} | {english_score:<8} | {average:.2f}"
            )

    print("-----------------------------------------------------------------------")


def add_student(book):
    """Thêm hồ sơ học sinh mới với info là tuple (toán, anh)."""
    while True:
        student_id = input("Nhập mã học sinh mới: ").strip()
        if find_student_index(book, student_id) != -1:
            print(f"Lỗi: Mã học sinh {student_id} đã tồn tại! Vui lòng nhập mã khác.")
            continue
        break

    name = input("Nhập tên học sinh: ").strip()
    math_score = input_score("Nhập điểm Toán: ")
    english_score = input_score("Nhập điểm Anh: ")

    book.append(
        {
            "id": student_id,
            "name": name,
            "info": (math_score, english_score),
        }
    )
    print(f"Thành công: Đã thêm học sinh {student_id} vào hệ thống!")


def update_scores(book):
    """
    Cập nhật điểm số bằng cách ghi đè tuple info mới.
    Tuple là immutable nên không thể sửa info[0] trực tiếp.
    """
    student_id = input("Nhập mã học sinh cần cập nhật: ").strip()
    index = find_student_index(book, student_id)

    if index == -1:
        print(f"Lỗi: Không tìm thấy học sinh có mã {student_id}!")
        return

    math_score = input_score("Nhập điểm Toán mới: ")
    english_score = input_score("Nhập điểm Anh mới: ")

    book[index]["info"] = (math_score, english_score)
    print(f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!")


def delete_student(book):
    """Xóa hồ sơ học sinh khỏi danh sách theo mã ID."""
    student_id = input("Nhập mã học sinh cần xóa: ").strip()
    index = find_student_index(book, student_id)

    if index == -1:
        print(f"Lỗi: Không tìm thấy học sinh có mã {student_id}!")
        return

    book.pop(index)
    print(f"Thành công: Đã xóa hồ sơ học sinh {student_id} khỏi hệ thống!")


def main():
    """Vòng lặp menu chính: hiển thị menu và gọi các hàm chức năng."""
    while True:
        print()
        display_menu()
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_grades(grade_book)
        elif choice == "2":
            add_student(grade_book)
        elif choice == "3":
            update_scores(grade_book)
        elif choice == "4":
            delete_student(grade_book)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    main()
