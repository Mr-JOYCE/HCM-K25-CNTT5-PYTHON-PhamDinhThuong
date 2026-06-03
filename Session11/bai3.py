product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

def menu():
    print("===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

def display_products():
    print("Danh sách sản phẩm hiện tại:")
    for i, product in enumerate(product_list, start=1):
        print(f"{i}. Mã SP: {product['product_id']} | Tên: {product['product_name']}, Giá: {product['price']}, Số lượng: {product['quantity']}")

def add_product():
    product_id = input("- Nhập mã sản phẩm: ").strip().upper()
    if any(p['product_id'] == product_id for p in product_list):
        print("Mã sản phẩm đã tồn tại. Vui lòng nhập mã khác.")
        return
    product_name = input("- Nhập tên sản phẩm: ")
    price = int(input("- Nhập giá sản phẩm: "))
    quantity = int(input("- Nhập số lượng sản phẩm: "))
    if price < 0 or quantity < 0:
        print("Giá và số lượng phải là số dương.")
        return
    new_product = {
        "product_id": product_id,
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    }
    product_list.append(new_product)
    print("Thêm sản phẩm thành công")

def update_product():
    product_id = input("- Nhập mã sản phẩm cần cập nhật: ").strip().upper()
    for product in product_list:
        if product['product_id'] == product_id:
            print(f"Thông tin hiện tại: Tên: {product['product_name']}, Giá: {product['price']}, Số lượng: {product['quantity']}")
            product_name = input("- Nhập tên sản phẩm mới (để trống nếu không đổi): ")
            price_input = input("- Nhập giá sản phẩm mới (để trống nếu không đổi): ")
            quantity_input = input("- Nhập số lượng sản phẩm mới (để trống nếu không đổi): ")
            if product_name:
                product['product_name'] = product_name
            if price_input:
                price = int(price_input)
                if price < 0:
                    print("Giá phải là số dương.")
                    return
                product['price'] = price
            if quantity_input:
                quantity = int(quantity_input)
                if quantity < 0:
                    print("Số lượng phải là số dương.")
                    return
                product['quantity'] = quantity
            print("Cập nhật sản phẩm thành công")
            return
    print("Không tìm thấy mã sản phẩm cần cập nhật!")

def delete_product():
    product_id = input("- Nhập mã sản phẩm cần xóa: ").strip().upper()
    for i, product in enumerate(product_list):
        if product['product_id'] == product_id:
            del product_list[i]
            print("Xóa sản phẩm thành công")
            return
    print("Không tìm thấy mã sản phẩm cần xóa!")

def main():
    while True:
        menu()
        choice = input("Chọn chức năng (1-5): ")
        if not choice.isdigit() or int(choice) not in range(1, 6):
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
        choice = int(choice)
        if choice == 1:
            display_products()
        elif choice == 2:
            add_product()
        elif choice == 3:
            update_product()
        elif choice == 4:
            delete_product()
        elif choice == 5:
            print("Thoát chương trình.Sau đó dừng chương trình")
            break


if __name__ == "__main__":
    main()