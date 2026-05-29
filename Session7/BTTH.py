raw_input = "   nGuyen vaN aN  ;  2004   "

CURRENT_YEAR = 2026


def display_menu():
    print('===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====')
    print('1. Hiển thị chuỗi dữ liệu gốc')
    print('2. Chuẩn hóa Họ tên và tính Tuổi')
    print('3. Tạo Mã ID và Email tự động')
    print('4. Thoát chương trình')
    print('=====================================')


def parse_raw_input(raw_string):
    """Tách chuỗi raw_input thành tên và năm sinh đã strip."""
    parts = raw_string.split(';')
    if len(parts) != 2:
        return None, None

    name = parts[0].strip().title()
    birth_year_str = parts[1].strip()
    return name, birth_year_str


def calculate_age(birth_year_str):
    """Tính tuổi thành viên dựa trên Năm hiện tại."""
    if not birth_year_str.isdigit():
        return None
    birth_year = int(birth_year_str)
    return CURRENT_YEAR - birth_year


def print_normalized_name_and_age():
    name, birth_year_str = parse_raw_input(raw_input)
    if name is None or birth_year_str is None:
        print('\nDữ liệu thô không hợp lệ.')
        return

    age = calculate_age(birth_year_str)
    if age is None:
        print('\nNăm sinh không hợp lệ.')
        return

    print('\nKết quả chuẩn hóa:')
    print(f"Họ tên: {name}")
    print(f"Tuổi: {age}")
    print()


def create_member_identity():
    """Tạo mã ID và email tự động từ tên và năm sinh."""
    name, birth_year_str = parse_raw_input(raw_input)
    if name is None or birth_year_str is None:
        print('\nDữ liệu thô không hợp lệ.')
        return

    name_parts = name.split()
    if len(name_parts) < 2 or not birth_year_str.isdigit():
        print('\nKhông thể tạo mã ID và email do dữ liệu không hợp lệ.')
        return

    last_name = name_parts[0]
    first_name = name_parts[-1]
    middle_name = name_parts[1] if len(name_parts) >= 3 else ''

    email_prefix = last_name[0] + (middle_name[0] if middle_name else '') + first_name
    email = email_prefix.lower() + '@company.com'

    id_suffix = birth_year_str[-2:]
    member_id = f"{first_name.upper()}{id_suffix}"

    width = 42
    print('\n===== THẺ THÀNH VIÊN =====')
    print('+' + '-' * (width - 2) + '+')
    print(f"| {'Mã ID:':<12}{member_id:<{width-15}}|")
    print(f"| {'Họ tên:':<12}{name:<{width-15}}|")
    print(f"| {'Email:':<12}{email:<{width-15}}|")
    print('+' + '-' * (width - 2) + '+')
    print()


def main():
    while True:
        display_menu()
        choice = input('Nhập lựa chọn của bạn (1-4): ')

        if not choice.isdigit() or int(choice) not in range(1, 5):
            print('\nLựa chọn không hợp lệ, vui lòng nhập lại!\n')
            continue

        option = int(choice)

        if option == 1:
            print('\nDữ liệu gốc:')
            print(raw_input)
            print()
        elif option == 2:
            print_normalized_name_and_age()
        elif option == 3:
            create_member_identity()
        else:
            print('\nChương trình kết thúc. Hẹn gặp lại!')
            break


if __name__ == '__main__':
    main()
