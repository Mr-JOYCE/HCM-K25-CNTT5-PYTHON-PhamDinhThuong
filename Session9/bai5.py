def display_order_list(order_list):
    if not order_list:
        print("Danh sách đơn hàng hiện đang trống.")
        return

    print("Danh sách đơn hàng hiện tại:")
    for index, order in enumerate(order_list, start=1):
        print(f"{index}. {order}")


def normalize_code(code):
    return code.strip().upper()


def find_order_index(order_list, order_code):
    normalized_code = normalize_code(order_code)
    for index, order in enumerate(order_list):
        if order.split(" - ")[0].strip().upper() == normalized_code:
            return index
    return None


def assign_driver(order_list):
    order_code = input("Nhập mã đơn hàng cần gán tài xế: ").strip()
    index = find_order_index(order_list, order_code)
    if index is None:
        print("Không tìm thấy mã đơn hàng.")
        return

    status = order_list[index].split(" - ")[1].strip().upper()
    if status != "PENDING":
        print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")
        return

    order_list[index] = f"{normalize_code(order_code)} - ASSIGNED"
    print("Đã gán tài xế cho đơn hàng.")


def update_delivery_status(order_list):
    order_code = input("Nhập mã đơn hàng cần cập nhật trạng thái: ").strip()
    index = find_order_index(order_list, order_code)
    if index is None:
        print("Không tìm thấy mã đơn hàng.")
        return

    order_code_norm, current_status = [part.strip() for part in order_list[index].split(" - ")]
    current_status = current_status.upper()

    if current_status == "PENDING":
        print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")
        return
    if current_status == "ASSIGNED":
        order_list[index] = f"{order_code_norm} - DELIVERING"
        print("Đã cập nhật đơn hàng sang DELIVERING.")
        return
    if current_status == "DELIVERING":
        order_list[index] = f"{order_code_norm} - COMPLETED"
        print("Đã cập nhật đơn hàng sang COMPLETED.")
        return
    if current_status == "COMPLETED":
        print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")
        return
    if current_status == "CANCELLED":
        print("Đơn hàng đã bị hủy, không thể cập nhật.")
        return


def cancel_order(order_list):
    order_code = input("Nhập mã đơn hàng cần hủy: ").strip()
    index = find_order_index(order_list, order_code)
    if index is None:
        print("Không tìm thấy mã đơn hàng.")
        return

    order_code_norm, current_status = [part.strip() for part in order_list[index].split(" - ")]
    current_status = current_status.upper()

    if current_status in {"PENDING", "ASSIGNED"}:
        order_list[index] = f"{order_code_norm} - CANCELLED"
        print("Đã hủy đơn hàng.")
        return
    if current_status == "DELIVERING":
        print("Đơn hàng đang được giao, không thể hủy.")
        return
    if current_status == "COMPLETED":
        print("Đơn hàng đã hoàn tất, không thể hủy.")
        return
    if current_status == "CANCELLED":
        print("Đơn hàng đã được hủy trước đó.")
        return


def main():
    order_list = [
        "GE001 - PENDING",
        "GE002 - ASSIGNED",
        "GE003 - DELIVERING",
    ]

    while True:
        print("===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
        print("1. Hiển thị danh sách đơn hàng")
        print("2. Gán tài xế cho đơn hàng")
        print("3. Cập nhật trạng thái giao hàng")
        print("4. Hủy đơn hàng")
        print("5. Thoát chương trình")

        choice = input("Chọn chức năng (1-5): ").strip()
        if choice == "1":
            display_order_list(order_list)
        elif choice == "2":
            assign_driver(order_list)
        elif choice == "3":
            update_delivery_status(order_list)
        elif choice == "4":
            cancel_order(order_list)
        elif choice == "5":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        print()


if __name__ == "__main__":
    main()
