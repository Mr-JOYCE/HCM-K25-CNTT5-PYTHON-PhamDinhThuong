staff = [
    {
        'id': 101,
        'name': 'Nguyen Van A',
        'salary': 5000000
    },
    {
        'id': 102,
        'name': 'Tran Thi B',
        'salary': 6000000
    },
    {
        'id': 103,
        'name': 'Le Van C',
        'salary': 5500000
    }
]

def menu():
    width = 42
    print('=' * width)
    print('QUẢN LÝ NHÂN SỰ - STAFF MANAGER'.center(width))
    print('=' * width)
    print("1. Thêm nhân viên mới")
    print("2. Danh sách nhân viên")
    print("3. Xóa nhân viên ra khỏi hệ thống")
    print("4. Thoát chương trình")
    print('=' * width)

def add_staff():
    id = staff[-1]['id'] + 1 if staff else 101
    name = input("Nhập tên nhân viên: ")
    if not name.strip():
        print("Tên nhân viên không được để trống.")
        return
    salary_input = input("Nhập lương nhân viên: ")
    try:
        salary = int(salary_input)
        if salary <= 0:
            print("Lương phải là số dương.")
            return
    except ValueError:
        print("Lương phải là một số nguyên.")
        return
    staff.append({'id': id, 'name': name, 'salary': salary})
    print(f"Thêm nhân viên thành công! ID: {id}")

def list_staff():
    if not staff:
        print("Chưa có dữ liệu nhân sự!")
        return
    print(f"{'ID':<6} | {'TÊN NHÂN VIÊN':<20} | {'MỨC LƯƠNG':<15}")
    for employee in staff:
        print(f"{employee['id']:<6} | {employee['name']:<20} | {employee['salary']:<15,}")

def delete_staff():
    try:
        id = int(input("Nhập ID nhân viên cần xóa: "))
    except ValueError:
        print("ID phải là một số nguyên.")
        return
    for employee in staff:
        if employee['id'] == id:
            staff.remove(employee)
            print(f"Đã xóa nhân viên có ID: {id} (Thành công)")
            return
    print(f"Không tìm thấy nhân viên để xóa")

def main():
    while True:
        menu()
        choice = input("Chọn chức năng (1-4): ")
        if choice == '1':
            add_staff()
        elif choice == '2':
            list_staff()
        elif choice == '3':
            delete_staff()
        elif choice == '4':
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()