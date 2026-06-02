def display_order_list(order_list):
    if not order_list:
        print("Danh sách đơn hàng hiện đang trống.")
        return

    print("Danh sách đơn hàng hiện tại:")
    for index, order in enumerate(order_list, start=1):
        print(f"{index}. {order}")


def format_order(order_code, status):
    return f"{order_code.strip().upper()} - {status.strip().upper()}"


def add_order(order_list):
    order_code = input("Nhập mã đơn hàng mới: ").strip()
    status = input("Nhập trạng thái đơn hàng: ").strip()

    if not order_code or not status:
        print("Mã đơn hàng và trạng thái không được để trống!")
        return

    order_list.append(format_order(order_code, status))
    print("Đã thêm đơn hàng mới.")


def get_position_input(prompt, max_position):
    position_input = input(prompt).strip()
    if not position_input.isdigit():
        print("Vị trí không hợp lệ!")
        return None

    position = int(position_input)
    if position < 1 or position > max_position:
        print("Không tồn tại đơn hàng ở vị trí này!")
        return None

    return position - 1


def edit_order(order_list):
    if not order_list:
        print("Danh sách đơn hàng hiện đang trống.")
        return

    position = get_position_input("Nhập vị trí cần sửa: ", len(order_list))
    if position is None:
        return

    order_code = input("Nhập mã đơn hàng mới: ").strip()
    status = input("Nhập trạng thái đơn hàng mới: ").strip()

    if not order_code or not status:
        print("Mã đơn hàng và trạng thái không được để trống!")
        return

    order_list[position] = format_order(order_code, status)
    print("Đã cập nhật đơn hàng.")


def delete_order(order_list):
    if not order_list:
        print("Danh sách đơn hàng hiện đang trống.")
        return

    position = get_position_input("Nhập vị trí cần xóa: ", len(order_list))
    if position is None:
        return

    removed_order = order_list.pop(position)
    print(f"Đã xóa đơn hàng: {removed_order}")


def update_menu(order_list):
    while True:
        print("----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
        print("1. Thêm đơn hàng mới")
        print("2. Sửa đơn hàng theo vị trí")
        print("3. Xóa đơn hàng theo vị trí")
        print("4. Quay lại menu chính")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            add_order(order_list)
        elif choice == "2":
            edit_order(order_list)
        elif choice == "3":
            delete_order(order_list)
        elif choice == "4":
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        print()


def count_orders_by_status(order_list):
    statuses = {
        "PENDING": 0,
        "DELIVERING": 0,
        "COMPLETED": 0,
        "CANCELLED": 0,
    }

    for order in order_list:
        parts = order.split(" - ")
        if len(parts) != 2:
            continue

        status = parts[1].strip().upper()
        if status in statuses:
            statuses[status] += 1

    print("===== THỐNG KÊ ĐƠN HÀNG =====")
    for status in ["PENDING", "DELIVERING", "COMPLETED", "CANCELLED"]:
        print(f"{status}: {statuses[status]}")
    print(f"Tổng số đơn hàng: {len(order_list)}")


def main():
    order_list = [
        "GE001 - PENDING",
        "GE002 - DELIVERING",
        "GE003 - CANCELLED",
    ]

    while True:
        print("===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
        print("1. Hiển thị danh sách đơn hàng")
        print("2. Cập nhật danh sách đơn hàng")
        print("3. Thống kê đơn hàng theo trạng thái")
        print("4. Thoát chương trình")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            display_order_list(order_list)
        elif choice == "2":
            update_menu(order_list)
        elif choice == "3":
            count_orders_by_status(order_list)
        elif choice == "4":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        print()


if __name__ == "__main__":
    main()
