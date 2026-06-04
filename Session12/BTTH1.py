cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]

def check_negative_value(value):
    if value < 0:
        print("Số lượng hoặc đơn giá không được âm.")
        return False
    return True



def menu():
    width = 52
    print("=" * width)
    print(" " + "SHOPEE CART MANAGER SYSTEM".center(width - 2) + " ")
    print("=" * width)
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("=" * width)

def view_cart():
    if not cart_items:
        print("Giỏ hàng của bạn đang trống.")
        return
    print("---- CHI TIẾT GIỎ HÀNG ----")
    total_price = 0
    print(f"{'STT'.center(4)} | {'Mã SP'.center(6)} | {'Tên sản phẩm'.center(20)} | {'Số lượng'.center(10)} | {'Đơn giá'.center(15)} | {'Thành tiền'.center(16)}")
    print("-" * 90)
    for i, item in enumerate(cart_items, start=1):
        item_total = item["number"] * item["price"]
        total_price += item_total
        print(f"{i:<4} | {item['id']:<6} | {item['name']:<20} | {item['number']:<10} | {item['price']:<15,} | {item_total:<16,}")
    print("-" * 90)
    print(f"Tổng số lượng sản phẩm trong giỏ: {sum(item['number'] for item in cart_items)}")
    print(f"Tổng tiền: {total_price:,}")

def add_product():
    product_id = input("Nhập mã sản phẩm: ").strip().upper()
    if any(item["id"] == product_id for item in cart_items):
        for item in cart_items:
            if item["id"] == product_id:
                additional_quantity = int(input("Sản phẩm đã tồn tại. Nhập số lượng muốn thêm: "))
                if not check_negative_value(additional_quantity):
                    return
                item["number"] += additional_quantity
                print(f"Đã cập nhật số lượng sản phẩm {item['name']} thành {item['number']}.")
                break
    else:
        product_name = input("Nhập tên sản phẩm: ")
        product_quantity = int(input("Nhập số lượng: "))
        product_price = int(input("Nhập đơn giá: "))
        if not check_negative_value(product_quantity) or not check_negative_value(product_price):
            return
        cart_items.append({
            "id": product_id,
            "name": product_name,
            "number": product_quantity,
            "price": product_price
        })
        print(f"Đã thêm sản phẩm {product_name} vào giỏ hàng.")

def update_quantity():
    product_id = input("Nhập mã sản phẩm cần cập nhật số lượng: ").strip().upper()
    product_quantity = int(input("Nhập số lượng mới: "))
    if not check_negative_value(product_quantity):
        return
    for item in cart_items:
        if item["id"] == product_id:
            item["number"] = product_quantity
            print(f"Đã cập nhật số lượng sản phẩm {item['name']} thành {item['number']}.")
            break
    else:
        print("Không tìm thấy sản phẩm với mã đã nhập.")

def delete_product():
    product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
    for item in cart_items:
        if item["id"] == product_id:
            cart_items.remove(item)
            print(f"Đã xóa sản phẩm {item['name']} khỏi giỏ hàng.")
            break
    else:
        print("Không tìm thấy sản phẩm với mã đã nhập.")

def main():
    while True:
        menu()
        choice = input("Mời bạn chọn chức năng (1-5): ")
        if choice == '1':
            view_cart()
        elif choice == '2':
            add_product()
        elif choice == '3':
            update_quantity()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý giỏ hàng. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()

