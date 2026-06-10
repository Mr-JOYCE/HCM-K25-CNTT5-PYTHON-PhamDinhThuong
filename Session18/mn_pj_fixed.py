PAID_STATUS = "Paid"
UNPAID_STATUS = "Unpaid"
DISCOUNT_THRESHOLD = 100_000_000
DISCOUNT_PERCENTAGE = 5


def display_orders(orders_list):
    """Chức năng 1: Duyệt qua danh sách dữ liệu và in ra toàn bộ đơn hàng dưới dạng bảng."""
    if not orders_list:
        print("\n[Lỗi]: Hệ thống hiện chưa có đơn hàng nào!")
        return

    print("\n" + "=" * 70)
    print(f"{'MÃ ĐƠN':<10} | {'TÊN ĐẠI LÝ':<25} | {'GIÁ TRỊ (VND)':>15} | {'TRẠNG THÁI':<12}")
    print("-" * 70)

    for order in orders_list:
        print(
            f"{order['id']:<10} | "
            f"{order['name']:<25} | "
            f"{order['price']:>15,} | "
            f"{order['status']:<12}"
        )

    print("=" * 70)


def input_non_empty_string(prompt_message):
    """Bắt buộc người dùng nhập chuỗi không được để trống."""
    while True:
        value = input(prompt_message).strip()

        if value:
            return value

        print("[Lỗi]: Thông tin này không được để trống! Vui lòng nhập lại.")


def input_positive_integer(prompt_message):
    """Bắt buộc người dùng nhập số nguyên dương lớn hơn 0 và chống crash."""
    while True:
        try:
            value = int(input(prompt_message))

            if value > 0:
                return value

            print("ERR-02 [Lỗi]: Giá trị đơn hàng phải là số tiền lớn hơn 0!")
        except ValueError:
            print("ERR-02 [Lỗi]: Giá trị đơn hàng phải là số tiền lớn hơn 0!")


def add_order(orders_list):
    """Chức năng 2: Tạo mới đơn hàng đại lý, validate dữ liệu và kiểm tra trùng mã."""
    print("\n--- TẠO MỚI ĐƠN HÀNG ---")

    order_id = input_non_empty_string("Nhập mã đơn hàng: ")

    for order in orders_list:
        if order["id"].upper() == order_id.upper():
            print("ERR-01 [Lỗi]: Mã đơn hàng này đã tồn tại trong hệ thống!")
            return

    order_name = input_non_empty_string("Nhập tên đại lý: ")
    order_price = input_positive_integer("Nhập giá trị đơn hàng (VND): ")

    new_order = {
        "id": order_id,
        "name": order_name,
        "price": order_price,
        "status": UNPAID_STATUS,
    }

    orders_list.append(new_order)
    print(f"[Thành công]: Đơn hàng {order_id} đã được tạo thành công!")


def update_order_status(orders_list):
    """Chức năng 3: Cập nhật trạng thái thanh toán từ Unpaid sang Paid."""
    print("\n--- CẬP NHẬT TRẠNG THÁI THANH TOÁN ---")

    if not orders_list:
        print("[Lỗi]: Hệ thống hiện chưa có đơn hàng nào!")
        return

    order_id = input_non_empty_string("Nhập mã đơn hàng cần cập nhật: ")

    for order in orders_list:
        if order["id"].upper() == order_id.upper():
            if order["status"] == PAID_STATUS:
                print("ERR-04 [Lỗi]: Đơn hàng này đã được thanh toán trước đó!")
                return

            order["status"] = PAID_STATUS
            print(f"[Thành công]: Đơn hàng {order['id']} đã được cập nhật trạng thái ĐÃ THANH TOÁN.")
            return

    print(f"ERR-03 [Lỗi]: Không tìm thấy đơn hàng nào có mã {order_id}!")


def calculate_revenue_and_discount(orders_list):
    """
    Chức năng 4: Chỉ tính toán doanh thu thực tế và chiết khấu.
    Trả về tuple gồm: tổng doanh thu, phần trăm chiết khấu, tiền chiết khấu.
    """
    total_revenue = 0

    for order in orders_list:
        if order["status"] == PAID_STATUS:
            total_revenue += order["price"]

    if total_revenue >= DISCOUNT_THRESHOLD:
        discount_percentage = DISCOUNT_PERCENTAGE
    else:
        discount_percentage = 0

    discount_amount = int(total_revenue * discount_percentage / 100)
    return total_revenue, discount_percentage, discount_amount


def main():
    """Hàm điều phối chính."""
    orders = [
        {"id": "HD01", "name": "Dai ly Hoang Long", "price": 45_000_000, "status": PAID_STATUS},
        {"id": "HD02", "name": "Tap hoa Minh Thu", "price": 15_000_000, "status": UNPAID_STATUS},
    ]

    while True:
        print("\n" + "=" * 20 + " HỆ THỐNG QUẢN LÝ ĐƠN HÀNG " + "=" * 20)
        print("1. Xem danh sách đơn hàng hiện có")
        print("2. Tạo mới đơn hàng đại lý")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & Chiết khấu")
        print("5. Thoát chương trình")
        print("=" * 67)

        try:
            choice = int(input("Mời chọn chức năng (1-5): "))
        except ValueError:
            print("ERR-05 [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5!")
            continue

        match choice:
            case 1:
                display_orders(orders)
            case 2:
                add_order(orders)
            case 3:
                update_order_status(orders)
            case 4:
                revenue, percentage, discount = calculate_revenue_and_discount(orders)

                print("\n--- BÁO CÁO DOANH THU & CHIẾT KHẤU ---")
                print(f"Tổng doanh thu thực tế (Đã thanh toán): {revenue:,} VND")
                print(f"Phần trăm chiết khấu áp dụng       : {percentage}%")
                print(f"Số tiền chiết khấu tương ứng      : {discount:,} VND")
            case 5:
                print("\nCảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
                break
            case _:
                print("ERR-05 [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5!")


if __name__ == "__main__":
    main()
