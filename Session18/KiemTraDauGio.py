def show_inventory(inventory_list):
    if not inventory_list:
        print("Kho hàng hiện đang trống!")
        return

    print("\n--- DANH SÁCH TỒN KHO ---")
    print(f"{'ID':<5} | {'Tên hàng hóa':<20} | {'Số lượng tồn'}")
    print("-" * 45)

    for item in inventory_list:
        print(f"{item['id']:<5} | {item['name']:<20} | {item['quantity']}")

    print("-" * 45)


def add_item(inventory_list):
    print("\n--- NHẬP HÀNG HÓA MỚI ---")

    while True:
        item_id = input("Nhập mã hàng hóa (ID): ").strip().upper()

        if item_id:
            break

        print("Mã hàng hóa không được để trống!")

    for item in inventory_list:
        if item["id"] == item_id:
            print("ID đã tồn tại trong kho!")
            return

    while True:
        item_name = input("Nhập tên hàng hóa: ").strip().title()

        if item_name:
            break

        print("Tên hàng hóa không được để trống!")

    while True:
        quantity = input("Nhập số lượng tồn kho: ").strip()

        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            break

        print("Số lượng phải là số nguyên lớn hơn 0!")

    new_item = {
        "id": item_id,
        "name": item_name,
        "quantity": quantity
    }

    inventory_list.append(new_item)

    print("Thêm hàng hóa vào kho thành công!")


def update_quantity(inventory_list):
    print("\n--- CẬP NHẬT SỐ LƯỢNG TỒN KHO ---")

    item_id = input("Nhập ID hàng hóa cần cập nhật: ").strip().upper()

    for item in inventory_list:

        if item["id"] == item_id:

            while True:
                new_quantity = input("Nhập số lượng mới: ").strip()

                if new_quantity.isdigit() and int(new_quantity) > 0:
                    item["quantity"] = int(new_quantity)

                    print("Cập nhật số lượng thành công!")
                    return

                print("Số lượng phải là số nguyên lớn hơn 0!")

    print(f"Không tìm thấy hàng hóa có mã {item_id}!")


def main():

    inventory = [
        {"id": "G01", "name": "Gạo Tẻ", "quantity": 50},
        {"id": "G02", "name": "Mì Tôm", "quantity": 120}
    ]

    while True:

        print("\n" + "=" * 40)
        print("QUẢN LÝ KHO HÀNG - GROCERY STORE")
        print("=" * 40)
        print("1. Xem danh sách tồn kho")
        print("2. Nhập thêm hàng mới")
        print("3. Cập nhật số lượng tồn kho theo ID")
        print("4. Thoát chương trình")
        print("=" * 40)

        try:
            choice = int(input("Mời bạn chọn chức năng (1-4): "))

        except ValueError:
            print("Bạn nhập không hợp lệ. Vui lòng nhập số từ 1 đến 4!")
            continue

        match choice:

            case 1:
                show_inventory(inventory)

            case 2:
                add_item(inventory)

            case 3:
                update_quantity(inventory)

            case 4:
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break

            case _:
                print("Bạn nhập không hợp lệ. Vui lòng nhập số từ 1 đến 4!")


if __name__ == "__main__":
    main()