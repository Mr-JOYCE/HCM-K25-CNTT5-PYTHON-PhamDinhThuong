product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]


def menu():
    print("===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

def display_products():
    print("Danh sách sản phẩm hiện tại:")
    for i, product in enumerate(product_list, start=1):
        print(f"{i}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | Giá: {product['price']} | Tồn kho: {product['quantity']} | Đã bán: {product['sold']} | Trang thái: {'Còn hàng' if product['quantity'] > 0 else 'Hết hàng'}")
    if len(product_list) == 0:
        print("Danh sách sản phẩm hiện đang trống")

def sell_product():
    input_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
    for product in product_list:
        if product['product_id'] == input_id:
            if product['quantity'] > 0:
                product['quantity'] -= 1
                product['sold'] += 1
                print(f"Số tiền khách phải trả: {product['price']:,} VND")
            else:
                print(f"Sản phẩm {product['product_name']} đã hết hàng. Không thể bán.")
            return
    print("Mã sản phẩm không tồn tại. Vui lòng nhập lại.")

def restock_product():
    product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
    for product in product_list:
        if product['product_id'] == product_id:
            quantity = int(input("Nhập số lượng cần nhập thêm: "))
            if quantity <= 0:
                print("Số lượng phải là số dương. Vui lòng nhập lại.")
                return
            product['quantity'] += quantity
            print(f"Đã nhập thêm {quantity} sản phẩm. Tồn kho hiện tại: {product['quantity']}")
            return
    print("Mã sản phẩm không tồn tại. Vui lòng nhập lại.")

def revenue_report():
    print("===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
    for i, product in enumerate(product_list, start=1):
        revenue = product['sold'] * product['price']
        print(f"{i}. {product['product_name']} | Đã bán: {product['sold']} | Doanh thu: {revenue:,} VND")

    total_revenue = sum(product['sold'] * product['price'] for product in product_list)
    print(f"Tổng doanh thu: {total_revenue:,} VND")
    
    print(f"Sản phẩm bán chạy nhất: {max(product_list, key=lambda x: x['sold'])['product_name']}")

def main():
    while True:
        menu()
        choice = input("Chọn chức năng (1-5): ").strip()
        if choice == '1':
            display_products()
        elif choice == '2':
            sell_product()
        elif choice == '3':
            restock_product()
        elif choice == '4':
            revenue_report()
        elif choice == '5':
            print("Thoat chương trình.Sau đó dừng chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()