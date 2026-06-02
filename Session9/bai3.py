def display_order_list(order_list):
    if not order_list:
        print("Danh sách đơn hàng hiện đang trống.")
        return

    print("Danh sách đơn hàng hiện tại:")
    for index, order_code in enumerate(order_list, start=1):
        print(f"{index}. {order_code}")


def add_order(order_list):
    order_code = input("Nhập mã đơn hàng mới: ").strip().upper()
    if not order_code:
        print("Mã đơn hàng không được để trống!")
        return

    order_list.append(order_code)
    print(f"Đã thêm đơn hàng: {order_code}")


def remove_order(order_list):
    if not order_list:
        print("Danh sách đơn hàng hiện đang trống.")
        return

    order_code = input("Nhập mã đơn hàng cần xóa: ").strip().upper()
    if order_code in order_list:
        order_list.remove(order_code)
        print(f"Đã xóa đơn hàng: {order_code}")
    else:
        print("Không tìm thấy mã đơn hàng cần xóa!")


def main():
    order_list = ["GE001", "GE002", "GE003"]

    while True:
        print("===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
        print("1. Hiển thị danh sách đơn hàng")
        print("2. Thêm đơn hàng mới")
        print("3. Xóa đơn hàng theo mã")
        print("4. Thoát chương trình")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            display_order_list(order_list)
        elif choice == "2":
            add_order(order_list)
        elif choice == "3":
            remove_order(order_list)
        elif choice == "4":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        print()


if __name__ == "__main__":
    main()
