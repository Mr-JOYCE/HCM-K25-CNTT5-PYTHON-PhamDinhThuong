inventory_stock = 100
total_revenue = 0.0

def menu():
    print(" TECHSTORE MANAGEMENT SYSTEM ".center(50, "="))
    print("1. Nhập thêm hàng vào kho")
    print("2. Bán hàng (Tính toán hóa đơn)")
    print("3. Xem báo cáo tổng quan")
    print("4. Thoát chương trình")
    print('=' * 50)

def add_stock() -> int:
    global inventory_stock
    while True:
        try:
            user_input = int(input("Nhập số lượng sản phẩm muốn thêm: "))
        except ValueError:
            print("Số lượng bạn nhập không hợp lệ. Vui lòng nhập lại!")
        else:
            inventory_stock += user_input
            print(f"Đã nhập thành công {user_input} sản phẩm")
            print(f"Tồn kho hiện tại: {inventory_stock}")
            break

def  process_sale(quantity) -> int:
    global inventory_stock, total_revenue
    if quantity > inventory_stock:
        return 
    
def calculate_final_price(quantity: int, price: float):
    global inventory_stock, total_revenue
    discount = 0.1

    total_price = quantity * price
    if total_price >= 1000:
        price_discount = total_price * discount
    else:
        price_discount = 0
    tax_VAT = (total_price - price_discount) * 0.08
    final_price = total_price + tax_VAT - price_discount
    inventory_stock -= quantity
    total_revenue += final_price
    return final_price, total_price, tax_VAT, price_discount

def sell_items():
    global inventory_stock, total_revenue
    while True:
        try:
            quantity_item = int(input("Nhập số lượng mua: "))
            price_item = int(input("Nhập đơn giá ($): "))
        except ValueError:
            print("Không hợp lệ vui lòng nhập lại!")
        else:
            if process_sale(quantity_item) is not None:
                print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
                return
            final_price, total_price, tax_VAT, price_discount = calculate_final_price(quantity_item, price_item)
            print("-> Hóa đơn chi tiết")
            print(f"Số lượng: {quantity_item} | Đơn giá: {price_item}")
            print(f"Tạm tính: ${total_price}")
            print(f"Giảm giá (10%): ${price_discount}")
            print(f"Thuế VAT (8%): ${tax_VAT}")
            print(f"Tổng thanh toán: ${final_price}")
            print("Đã bán thành công!")
            break
            
def print_report():
    global inventory_stock, total_revenue
    print(f"Tồng kho hiện tại: {inventory_stock}")
    print(f"Tỏng doanh thu: {total_revenue}")

def main():
    while True:
        menu()
        choice = input("Chọn chức năng (1-4): ")
        if not choice.isdigit() or int(choice) not in range(1, 5):
            print("Lựa chọn không hợp lệ vui lòng nhập lại!")
            continue
        if choice == "1":
            print("--- Nhập hàng ---")
            add_stock()
        if choice == "2":
            print("--- Bán hàng ---")
            sell_items()
        if choice == "3":
            print("--- Báo cáo kinh doanh ---")
            print_report()
        if choice == "4":
            print("Thoát chương trình")
            break

        

if __name__ == "__main__":
    main()
