def show_orders(orders_list):
    if not orders_list:
        print("Hệ thống hiện chưa có đơn hàng nào!")
        return

    print("—— DANH SÁCH ĐƠN HÀNG ĐẠI LÝ ——")

    col_id = max(len("MÃ ĐƠN"), max(len(order["id"]) for order in orders_list))
    col_name = max(len("TÊN ĐẠI LÝ"), max(len(order["name"]) for order in orders_list))
    col_price = max(len("GIÁ TRỊ (VND)"), max(len(str(order["price"])) for order in orders_list))
    col_status = max(len("TRẠNG THÁI"), max(len(order["status"]) for order in orders_list))

    separator = (
        f"{'-' * col_id}-+-{'-' * col_name}-+-{'-' * col_price}-+-{'-' * col_status}"
    )

    print(
        f"{'MÃ ĐƠN':<{col_id}} | {'TÊN ĐẠI LÝ':<{col_name}} | "
        f"{'GIÁ TRỊ (VND)':>{col_price}} | {'TRẠNG THÁI':<{col_status}}"
    )
    print(separator)

    for order in orders_list:
        print(
            f"{order['id']:<{col_id}} | {order['name']:<{col_name}} | "
            f"{order['price']:>{col_price}} | {order['status']:<{col_status}}"
        )


def create_order(orders_list):
    print("—— TẠO MỚI ĐƠN HÀNG ——")

    while True:
        order_id = input("Nhập mã đơn hàng: ").strip()
        if order_id:
            break

    for order in orders_list:
        if order["id"] == order_id:
            print("[Lỗi]: Mã đơn hàng này đã tồn tại trong hệ thống! (ERR-01)")
            return

    while True:
        agent_name = input("Nhập tên đại lý: ").strip()
        if agent_name:
            break

    while True:
        price_input = input("Nhập giá trị đơn hàng (VND): ").strip()
        try:
            price = int(price_input)
            if price > 0:
                break
            print("[Lỗi]: Giá trị đơn hàng phải là số tiền lớn hơn 0! (ERR-02)")
        except ValueError:
            print("[Lỗi]: Giá trị đơn hàng phải là số tiền lớn hơn 0! (ERR-02)")

    new_order = {
        "id": order_id,
        "name": agent_name,
        "price": price,
        "status": "Unpaid",
    }
    orders_list.append(new_order)
    print(f"[Thành công]: Đơn hàng {order_id} đã được tạo thành công!")


def update_payment_status(orders_list):
    print("—— CẬP NHẬT TRẠNG THÁI THANH TOÁN ——")

    order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip()

    for order in orders_list:
        if order["id"] == order_id:
            if order["status"] == "Paid":
                print("[Lỗi]: Đơn hàng này đã được thanh toán trước đó! (ERR-04)")
                return

            print(
                f"Tìm thấy đơn hàng của: {order['name']} "
                f"(Giá trị: {order['price']})"
            )
            order["status"] = "Paid"
            print(
                f"[Thành công]: Đơn hàng {order_id} đã được cập nhật "
                "trạng thái ĐÃ THANH TOÁN!"
            )
            return

    print(f"[Lỗi]: Không tìm thấy đơn hàng nào có mã [{order_id}]! (ERR-03)")


def calculate_financials(orders_list):
    total_revenue = sum(
        order["price"] for order in orders_list if order["status"] == "Paid"
    )

    if total_revenue >= 100_000_000:
        discount_percent = 5
    else:
        discount_percent = 0

    discount_amount = int(total_revenue * discount_percent / 100)
    return total_revenue, discount_percent, discount_amount


def main():
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    orders = [
        {"id": "HD01", "name": "Dai ly Hoang Long", "price": 45000000, "status": "Paid"},
        {"id": "HD02", "name": "Tap hoa Minh Thu", "price": 15000000, "status": "Unpaid"},
    ]

    while True:
        print("=" * 45)
        print("QUẢN LÝ ĐƠN HÀNG - AGENT ORDER")
        print("1. Xem danh sách đơn hàng hiện có")
        print("2. Tạo mới đơn hàng đại lý")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & Chiết khấu")
        print("5. Thoát chương trình")
        print("=" * 45)

        try:
            choice = int(input("Mời chọn chức năng (1-5): ").strip())
        except ValueError:
            print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5! (ERR-05)")
            continue

        if choice == 1:
            show_orders(orders)
        elif choice == 2:
            create_order(orders)
        elif choice == 3:
            update_payment_status(orders)
        elif choice == 4:
            print("—— TÍNH TỔNG DOANH THU & CHIẾT KHẤU ——")
            total_revenue, discount_percent, discount_amount = calculate_financials(orders)
            print(f"Tổng doanh thu thực tế: {total_revenue} VND")
            print(f"Phần trăm chiết khấu: {discount_percent}%")
            print(f"Số tiền chiết khấu: {discount_amount} VND")
        elif choice == 5:
            print("Cảm ơn bạn đã sử dụng hệ thống Quản lý Đơn hàng. Tạm biệt!")
            break
        else:
            print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5! (ERR-05)")


if __name__ == "__main__":
    main()
