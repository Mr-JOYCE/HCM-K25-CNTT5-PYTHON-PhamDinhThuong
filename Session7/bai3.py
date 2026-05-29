raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "


def normalize_phone(phone_raw):
    """Chuẩn hóa số điện thoại và kiểm tra định dạng."""
    phone = phone_raw.strip().replace('-', '')

    if not phone.isdigit():
        return "Invalid Format"

    masked_phone = "******" + phone[6:]
    return masked_phone


def parse_raw_data(raw_data_string):
    """Chuyển raw_data thành danh sách nhân viên đã chuẩn hóa."""
    employees = []
    raw_records = raw_data_string.split('|')

    for record in raw_records:
        fields = record.split(';')
        if len(fields) != 4:
            continue

        emp_id = fields[0].strip().upper()
        full_name = fields[1].strip().title()
        phone = normalize_phone(fields[2])
        department = fields[3].strip().upper()

        employees.append({
            'id': emp_id,
            'name': full_name,
            'phone': phone,
            'department': department,
        })

    return employees


def print_raw_data():
    """Hiển thị chuỗi dữ liệu gốc."""
    print('\nChuỗi dữ liệu gốc:')
    print(raw_data)
    print()


def print_employee_report(employees):
    """In báo cáo nhân sự đã chuẩn hóa dưới dạng bảng."""
    print()
    print('BÁO CÁO NHÂN SỰ')
    print('-' * 70)
    print(f"{'ID':<10}{'Họ tên':<25}{'Phòng ban':<15}{'Số điện thoại':<20}")
    print('-' * 70)

    for emp in employees:
        print(f"{emp['id']:<10}{emp['name']:<25}{emp['department']:<15}{emp['phone']:<20}")

    print('-' * 70)
    print()


def search_employee_by_id(employees):
    """Tìm kiếm nhân viên theo mã ID đã chuẩn hóa."""
    search_input = input('Nhập mã nhân viên cần tìm: ')
    search_id = search_input.strip().upper()

    for emp in employees:
        if emp['id'] == search_id:
            print('\nThông tin nhân viên tìm được:')
            print(f"Mã ID: {emp['id']}")
            print(f"Họ tên: {emp['name']}")
            print(f"Phòng ban: {emp['department']}")
            print(f"Số điện thoại: {emp['phone']}")
            print()
            return

    print('\nKhông tìm thấy nhân viên')
    print()


def display_menu():
    """Hiển thị menu chính của chương trình."""
    print('===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====')
    print('1. Hiển thị chuỗi dữ liệu gốc')
    print('2. Chuẩn hóa dữ liệu và in báo cáo')
    print('3. Tìm kiếm nhân viên theo mã ID')
    print('4. Thoát chương trình')


def main():
    employees = parse_raw_data(raw_data)

    while True:
        display_menu()
        choice = input('Chọn chức năng (1-4): ')

        if not choice.isdigit() or int(choice) not in range(1, 5):
            print('\nLựa chọn không hợp lệ, vui lòng nhập lại!\n')
            continue

        option = int(choice)

        if option == 1:
            print_raw_data()
        elif option == 2:
            print_employee_report(employees)
        elif option == 3:
            search_employee_by_id(employees)
        else:
            print('\nThoát chương trình')
            break


if __name__ == '__main__':
    main()
