"""
BTTH1 - He thong Quan Ly Gio Hang Shopee (CLI)

1) PHAN TICH INPUT / OUTPUT
Input:
- cart_items: list[list] (du lieu ban dau trong code)
  Moi san pham co cau truc: [ma_sp: str, ten_sp: str, so_luong: int, don_gia: int]
- Nguoi dung nhap tu ban phim:
  + Lua chon menu (1-5)
  + Chuc nang 2: ma_sp, ten_sp, so_luong, don_gia
  + Chuc nang 3: ma_sp, so_luong_moi
  + Chuc nang 4: ma_sp

Output:
- Hien thi menu CLI.
- In bang chi tiet gio hang.
- Tong so luong san pham trong gio.
- Tong thanh toan.
- Thong bao thanh cong/that bai theo tung thao tac.

2) DE XUAT GIAI PHAP
- Tach chuong trinh thanh cac ham:
  + display_menu(): hien thi menu.
  + show_cart_details(cart_items): in bang + tinh tong.
  + find_item_index_by_id(cart_items, product_id): tim vi tri san pham.
  + add_or_increase_product(cart_items): them moi hoac cong don so luong.
  + update_product_quantity(cart_items): cap nhat so luong.
  + remove_product(cart_items): xoa san pham khoi gio.
  + input_positive_int(...), input_non_negative_int(...): validate du lieu so.
- Xu ly edge cases:
  + So luong <= 0 (khi them/sua): bao loi, khong cap nhat.
  + Don gia < 0 (khi them): bao loi, khong cap nhat.
  + Ma sp khong ton tai (cap nhat/xoa): thong bao theo de bai.
  + Menu khong hop le (khong phai 1-5): thong bao loi.

3) PSEUDOCODE
BEGIN
  khoi tao cart_items mau
  LOOP vo han:
    hien thi menu
    nhap choice
    IF choice == "1": xem chi tiet gio hang
    ELIF choice == "2": them hoac cong don so luong
    ELIF choice == "3": cap nhat so luong
    ELIF choice == "4": xoa san pham
    ELIF choice == "5": thoat vong lap
    ELSE: thong bao lua chon khong hop le
END
"""


def format_currency(value: int) -> str:
    return f"{value:,}d"


def display_menu() -> None:
    print("\n" + "=" * 62)
    print("               SHOPEE CART MANAGEMENT SYSTEM")
    print("=" * 62)
    print("[1] Xem chi tiet gio hang & Tinh tong tien")
    print("[2] Them san pham moi / Cong don so luong")
    print("[3] Cap nhat so luong cua mot san pham")
    print("[4] Xoa san pham khoi gio hang")
    print("[5] Thoat chuong trinh")
    print("=" * 62)


def find_item_index_by_id(cart_items: list[list], product_id: str) -> int:
    """Tra ve index cua san pham theo ma, neu khong co thi tra ve -1."""
    for index, item in enumerate(cart_items):
        if item[0].lower() == product_id.lower():
            return index
    return -1


def input_positive_int(prompt: str) -> int | None:
    """Nhap so nguyen duong (> 0). Sai thi tra ve None."""
    raw_value = input(prompt).strip()
    try:
        value = int(raw_value)
    except ValueError:
        print("Du lieu khong hop le. Vui long nhap so nguyen.")
        return None

    if value <= 0:
        print("Loi: So luong phai lon hon 0.")
        return None
    return value


def input_non_negative_int(prompt: str) -> int | None:
    """Nhap so nguyen khong am (>= 0). Sai thi tra ve None."""
    raw_value = input(prompt).strip()
    try:
        value = int(raw_value)
    except ValueError:
        print("Du lieu khong hop le. Vui long nhap so nguyen.")
        return None

    if value < 0:
        print("Loi: Don gia khong duoc am.")
        return None
    return value


def show_cart_details(cart_items: list[list]) -> None:
    """In chi tiet gio hang va tong tien."""
    print("\n--- CHI TIET GIO HANG ---")
    if not cart_items:
        print("Gio hang dang trong.")
        return

    print("-" * 96)
    print(
        f"{'STT':<4} | {'Ma SP':<8} | {'Ten San Pham':<30} | "
        f"{'SL':<5} | {'Don Gia':<14} | {'Thanh Tien':<14}"
    )
    print("-" * 96)

    total_quantity = 0
    total_amount = 0

    for index, item in enumerate(cart_items, start=1):
        product_id, product_name, quantity, unit_price = item
        line_total = quantity * unit_price
        total_quantity += quantity
        total_amount += line_total

        print(
            f"{index:<4} | {product_id:<8} | {product_name:<30} | "
            f"{quantity:<5} | {format_currency(unit_price):<14} | {format_currency(line_total):<14}"
        )

    print("-" * 96)
    print(f"=> Tong so luong san pham trong gio: {total_quantity}")
    print(f"=> TONG TIEN THANH TOAN: {format_currency(total_amount)}")


def add_or_increase_product(cart_items: list[list]) -> None:
    """Them san pham moi hoac cong don so luong neu da ton tai ma."""
    print("\n--- THEM SAN PHAM / CONG DON SO LUONG ---")
    product_id = input("Nhap ma san pham: ").strip()
    product_name = input("Nhap ten san pham: ").strip()

    quantity = input_positive_int("Nhap so luong: ")
    if quantity is None:
        return

    unit_price = input_non_negative_int("Nhap don gia: ")
    if unit_price is None:
        return

    existing_index = find_item_index_by_id(cart_items, product_id)
    if existing_index != -1:
        cart_items[existing_index][2] += quantity
        print("San pham da ton tai. Da cong don so luong thanh cong.")
    else:
        cart_items.append([product_id, product_name, quantity, unit_price])
        print("Da them san pham moi vao gio hang.")


def update_product_quantity(cart_items: list[list]) -> None:
    """Cap nhat so luong moi cua mot san pham theo ma."""
    print("\n--- CAP NHAT SO LUONG SAN PHAM ---")
    product_id = input("Nhap ma san pham can cap nhat: ").strip()

    index = find_item_index_by_id(cart_items, product_id)
    if index == -1:
        print("Ma san pham khong ton tai trong gio hang.")
        return

    new_quantity = input_positive_int("Nhap so luong moi: ")
    if new_quantity is None:
        return

    cart_items[index][2] = new_quantity
    print("Cap nhat so luong thanh cong.")


def remove_product(cart_items: list[list]) -> None:
    """Xoa hoan toan mot san pham khoi gio hang theo ma."""
    print("\n--- XOA SAN PHAM KHOI GIO HANG ---")
    product_id = input("Nhap ma san pham can xoa: ").strip()

    index = find_item_index_by_id(cart_items, product_id)
    if index == -1:
        print("Ma san pham khong ton tai trong gio hang.")
        return

    removed_item = cart_items.pop(index)
    print(f"Da xoa san pham: {removed_item[1]} ({removed_item[0]}).")


def main() -> None:
    """Ham dieu khien chuong trinh chinh."""
    cart_items = [
        ["P001", "Dien thoai iPhone 15", 1, 25000000],
        ["P002", "Op lung Silicon", 2, 150000],
    ]

    while True:
        display_menu()
        choice = input("Moi ban chon chuc nang (1-5): ").strip()

        if choice == "1":
            show_cart_details(cart_items)
        elif choice == "2":
            add_or_increase_product(cart_items)
        elif choice == "3":
            update_product_quantity(cart_items)
        elif choice == "4":
            remove_product(cart_items)
        elif choice == "5":
            print("Cam on ban da su dung chuong trinh. Tam biet!")
            break
        else:
            print("Lua chon khong hop le. Vui long nhap so tu 1 den 5.")


if __name__ == "__main__":
    main()
