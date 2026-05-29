def normalize_registration(raw_line):
    """Chuẩn hóa một phiếu đăng ký nếu dữ liệu hợp lệ.

    Trả về một dict chứa dữ liệu đã chuẩn hóa,
    hoặc None nếu phiếu không hợp lệ.
    """
    raw_line = raw_line.strip()
    parts = raw_line.split('|')

    if len(parts) != 4:
        print('Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này')
        return None

    student_name = parts[0].strip().title()
    course_name = parts[1].strip().title()
    student_code = parts[2].strip().upper()
    email = parts[3].strip().lower()

    if '@' not in email:
        print('Email không hợp lệ. Bỏ qua phiếu này')
        return None

    if len(student_code) < 5:
        print('Mã học viên không hợp lệ. Bỏ qua phiếu này')
        return None

    confirmation_code = f"{student_code}_{course_name.upper().replace(' ', '-') }"

    return {
        'student_name': student_name,
        'course_name': course_name,
        'student_code': student_code,
        'email': email,
        'confirmation_code': confirmation_code,
    }


def print_normalized_registration(registration):
    """In phiếu đăng ký đã chuẩn hóa theo định dạng yêu cầu."""
    print('\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====')
    print(f"Học viên: {registration['student_name']}")
    print(f"Khóa học: {registration['course_name']}")
    print(f"Mã học viên: {registration['student_code']}")
    print(f"Email: {registration['email']}")
    print(f"Mã xác nhận: {registration['confirmation_code']}")


def main():
    try:
        quantity_input = input('Nhập số lượng phiếu đăng ký cần xử lý: ')
        quantity = int(quantity_input)
    except ValueError:
        print('Số lượng phiếu đăng ký không hợp lệ')
        return

    if quantity <= 0:
        print('Số lượng phiếu đăng ký không hợp lệ')
        return

    for index in range(1, quantity + 1):
        raw_line = input(f'Nhập phiếu đăng ký thứ {index}: ')
        registration = normalize_registration(raw_line)

        if registration is None:
            continue

        print_normalized_registration(registration)


if __name__ == '__main__':
    main()
