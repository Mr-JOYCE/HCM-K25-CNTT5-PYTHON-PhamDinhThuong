from datetime import datetime

parking_lot = []
next_vehicle_id = 1

ERR_DUPLICATE = "[Lỗi]: Xe với biển số này đã tồn tại trong bãi!"
ERR_INVALID_TYPE = "[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!"
ERR_INVALID_EXIT_TIME = "[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!"
ERR_NOT_FOUND = "[Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!"
ERR_INVALID_MENU = "[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!"
ERR_EMPTY_PARKING = "[Lỗi]: Bãi xe hiện đang trống!"


def display_menu():
    width = 58
    print("=" * width)
    print("HỆ THỐNG QUẢN LÝ BÃI ĐỖ XE THÔNG MINH".center(width))
    print("=" * width)
    print("1. Check-in")
    print("2. Báo cáo tồn kho")
    print("3. Tìm kiếm xe")
    print("4. Check-out")
    print("5. Thoát")
    print("=" * width)


def normalize_plate(plate):
    return plate.strip().upper()


def get_plate_input(prompt):
    while True:
        plate = input(prompt).strip()
        if plate:
            return normalize_plate(plate)
        print("[Lỗi]: Biển số không được để trống.")


def get_vehicle_type():
    while True:
        vehicle_type = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
        if not vehicle_type:
            print("[Lỗi]: Loại xe không được để trống.")
            continue
        try:
            type_int = int(vehicle_type)
        except ValueError:
            print(ERR_INVALID_TYPE)
            continue
        if type_int in (1, 2):
            return type_int
        print(ERR_INVALID_TYPE)


def get_exit_time(entry_time):
    while True:
        raw_exit = input("Nhập giờ ra (0-24): ").strip()
        if not raw_exit:
            print("[Lỗi]: Giờ ra không được để trống.")
            continue
        try:
            exit_time = int(raw_exit)
        except ValueError:
            print("[Lỗi]: Giờ ra phải là một số nguyên.")
            continue
        if exit_time < entry_time:
            print(ERR_INVALID_EXIT_TIME)
            continue
        if exit_time < 0 or exit_time > 24:
            print("[Lỗi]: Giờ ra phải nằm trong khoảng 0-24.")
            continue
        return exit_time


def find_vehicle_by_plate(plate):
    for vehicle in parking_lot:
        if vehicle["plate"] == plate:
            return vehicle
    return None


def check_in():
    global next_vehicle_id
    plate = get_plate_input("Nhập biển số: ")
    if find_vehicle_by_plate(plate) is not None:
        print(ERR_DUPLICATE)
        return
    vehicle_type = get_vehicle_type()
    entry_time = datetime.now().hour
    vehicle = {
        "id": next_vehicle_id,
        "plate": plate,
        "type": vehicle_type,
        "entry_time": entry_time,
    }
    parking_lot.append(vehicle)
    next_vehicle_id += 1
    print("[Thông báo]: Check-in thành công!")
    print(f"ID: {vehicle['id']}")
    print(f"Biển số: {vehicle['plate']}")
    print(f"Loại xe: {'Xe máy' if vehicle_type == 1 else 'Ô tô'}")
    print(f"Giờ vào: {vehicle['entry_time']}")


def report_inventory():
    if not parking_lot:
        print(ERR_EMPTY_PARKING)
        return
    print("{:^58}".format("DANH SÁCH PHƯƠNG TIỆN ĐANG ĐỖ"))
    print("-" * 58)
    print(f"{'ID':<4} {'BIỂN SỐ':<14} {'LOẠI XE':<10} {'GIỜ VÀO':<8}")
    print("-" * 58)
    for vehicle in parking_lot:
        type_label = 'Xe máy' if vehicle['type'] == 1 else 'Ô tô'
        print(f"{vehicle['id']:<4} {vehicle['plate']:<14} {type_label:<10} {vehicle['entry_time']:<8}")


def search_vehicle():
    plate = get_plate_input("Nhập biển số cần tìm: ")
    vehicle = find_vehicle_by_plate(plate)
    if vehicle is None:
        print(ERR_NOT_FOUND.format(plate=plate))
        return
    print("[Kết quả tìm kiếm]")
    print(f"ID: {vehicle['id']}")
    print(f"Biển số: {vehicle['plate']}")
    print(f"Loại xe: {'Xe máy' if vehicle['type'] == 1 else 'Ô tô'}")
    print(f"Giờ vào: {vehicle['entry_time']}")


def check_out():
    plate = get_plate_input("Nhập biển số cần checkout: ")
    vehicle = find_vehicle_by_plate(plate)
    if vehicle is None:
        print(ERR_NOT_FOUND.format(plate=plate))
        return
    exit_time = get_exit_time(vehicle['entry_time'])
    duration = exit_time - vehicle['entry_time']
    rate = 2000 if vehicle['type'] == 1 else 5000
    total_fee = duration * rate
    parking_lot.remove(vehicle)
    print("[Thanh toán thành công]")
    print(f"Biển số: {vehicle['plate']}")
    print(f"Loại xe: {'Xe máy' if vehicle['type'] == 1 else 'Ô tô'}")
    print(f"Giờ vào: {vehicle['entry_time']}")
    print(f"Giờ ra: {exit_time}")
    print(f"Thời gian đậu: {duration} giờ")
    print(f"Phí thanh toán: {total_fee:,} VNĐ")


def main():
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-5): ").strip()
        if not choice.isdigit() or choice not in {'1', '2', '3', '4', '5'}:
            print(ERR_INVALID_MENU)
            continue
        if choice == '1':
            check_in()
        elif choice == '2':
            report_inventory()
        elif choice == '3':
            search_vehicle()
        elif choice == '4':
            check_out()
        elif choice == '5':
            print("Thoát chương trình. Hẹn gặp lại!")
            break


if __name__ == '__main__':
    main()
