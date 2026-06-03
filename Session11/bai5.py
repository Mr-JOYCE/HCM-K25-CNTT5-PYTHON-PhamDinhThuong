product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]


def normalize_product_id(product_id: str) -> str:
    return product_id.strip().upper()


def find_product_by_id(product_id: str):
    """Tìm sản phẩm theo mã sản phẩm đã chuẩn hóa."""
    normalized_id = normalize_product_id(product_id)
    for product in product_list:
        if product["product_id"] == normalized_id:
            return product
    return None


def format_price(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:.2f}"


def get_positive_int(prompt_message: str):
    value = input(prompt_message).strip()
    if not value.isdigit():
        return None
    result = int(value)
    return result if result > 0 else None


def get_int_in_range(prompt_message: str, minimum: int, maximum: int):
    value = input(prompt_message).strip()
    if not value.isdigit():
        return None
    number = int(value)
    if number < minimum or number > maximum:
        return None
    return number


def get_product_status(quantity: int) -> str:
    if quantity == 0:
        return "Hết hàng"
    if quantity <= 5:
        return "Sắp hết hàng"
    return "Còn hàng"


def display_product_list():
    if not product_list:
        print("Danh sách sản phẩm hiện đang trống.")
        return

    print("Danh sách sản phẩm hiện tại:")
    for index, product in enumerate(product_list, start=1):
        status = get_product_status(product["quantity"])
        print(
            f"{index}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | Giá: {product['price']} | "
            f"Tồn kho: {product['quantity']} | Đã bán: {product['sold']} | Đổi trả: {product['returned']} | "
            f"Giảm giá: {product['discount']}% | Trạng thái: {status}"
        )


def sell_product():
    product_id = normalize_product_id(input("Nhập mã sản phẩm khách muốn mua: "))
    product = find_product_by_id(product_id)
    if not product:
        print("Không tìm thấy sản phẩm cần bán")
        return

    quantity_to_sell = get_positive_int("Nhập số lượng khách mua: ")
    if quantity_to_sell is None:
        print("Số lượng mua không hợp lệ")
        return

    if quantity_to_sell > product["quantity"]:
        print("Số lượng trong kho không đủ để bán")
        return

    product["quantity"] -= quantity_to_sell
    product["sold"] += quantity_to_sell
    discounted_price = product["price"] * (100 - product["discount"]) / 100
    total_amount = discounted_price * quantity_to_sell
    print(
        f"Tổng tiền khách cần thanh toán: {format_price(total_amount)}"
    )


def process_return():
    product_id = normalize_product_id(input("Nhập mã sản phẩm khách muốn đổi/trả: "))
    product = find_product_by_id(product_id)
    if not product:
        print("Không tìm thấy sản phẩm cần đổi trả")
        return

    quantity_to_return = get_positive_int("Nhập số lượng đổi/trả: ")
    if quantity_to_return is None:
        print("Số lượng đổi/trả không hợp lệ")
        return

    if quantity_to_return > product["sold"]:
        print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
        return

    product["sold"] -= quantity_to_return
    product["quantity"] += quantity_to_return
    product["returned"] += quantity_to_return
    discounted_price = product["price"] * (100 - product["discount"]) / 100
    refund_amount = discounted_price * quantity_to_return
    print(f"Số tiền hoàn lại: {format_price(refund_amount)}")


def apply_discount():
    product_id = normalize_product_id(input("Nhập mã sản phẩm cần áp dụng giảm giá: "))
    product = find_product_by_id(product_id)
    if not product:
        print("Không tìm thấy sản phẩm cần giảm giá")
        return

    discount_percent = get_int_in_range("Nhập phần trăm giảm giá: ", 0, 70)
    if discount_percent is None:
        print("Phần trăm giảm giá không hợp lệ")
        return

    product["discount"] = discount_percent
    print(f"Đã cập nhật giảm giá cho sản phẩm {product['product_id']} thành {product['discount']}%")


def restock_product():
    product_id = normalize_product_id(input("Nhập mã sản phẩm cần nhập thêm: "))
    product = find_product_by_id(product_id)
    if not product:
        print("Không tìm thấy sản phẩm cần nhập thêm")
        return

    added_quantity = get_positive_int("Nhập số lượng nhập thêm: ")
    if added_quantity is None:
        print("Số lượng nhập thêm không hợp lệ")
        return

    product["quantity"] += added_quantity
    print(f"Đã nhập thêm {added_quantity} sản phẩm cho {product['product_id']}. Tồn kho hiện tại: {product['quantity']}")


def show_menu():
    print("===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")


def main():
    while True:
        show_menu()
        choice = input("Chọn chức năng (1-6): ").strip()
        if not choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            continue

        choice_number = int(choice)
        if choice_number == 1:
            display_product_list()
        elif choice_number == 2:
            sell_product()
        elif choice_number == 3:
            process_return()
        elif choice_number == 4:
            apply_discount()
        elif choice_number == 5:
            restock_product()
        elif choice_number == 6:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    main()

