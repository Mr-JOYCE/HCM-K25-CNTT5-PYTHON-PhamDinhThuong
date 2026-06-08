available_seats = 50  
flight_revenue = 0.0  
BASE_PRICE = 2000.0   

def calculate_ticket_price(quantity, ticket_class):
    if ticket_class == 1:
        unit_price = BASE_PRICE
    elif ticket_class == 2:
        unit_price = BASE_PRICE * 1.5
    else:
        unit_price = BASE_PRICE
    
    subtotal = unit_price * quantity
    service_fee = subtotal * 0.05
    final_price = subtotal + service_fee
    
    return final_price


def process_booking(quantity, total_price):
    global available_seats, flight_revenue
    
    available_seats -= quantity
    flight_revenue += total_price


def process_refund(quantity):
    global available_seats, flight_revenue
    
    refund_amount = (BASE_PRICE * 0.80) * quantity
    
    available_seats += quantity
    flight_revenue -= refund_amount
    
    return refund_amount


def display_flight_status():
    booked_seats = 50 - available_seats
    
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue:,.2f}")

def main():
    global available_seats
    
    while True:
        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("=============================================")
        
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == '1':
            print("--- ĐẶT VÉ MÁY BAY ---")
            try:
                qty_input = input("Nhập số lượng vé: ")
                quantity = int(qty_input)
            except ValueError:
                print("Đầu vào không hợp lệ.")
                continue
            
            if quantity <= 0:
                print("Số tiền không hợp lệ")
                continue
            
            if quantity > available_seats:
                print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
                continue
                
            try:
                class_input = input("Chọn hạng vé (1: Economy, 2: Business): ")
                ticket_class = int(class_input)
            except ValueError:
                print("Đầu vào không hợp lệ.")
                continue
            
            if ticket_class not in [1, 2]:
                print("Hạng vé không hợp lệ. Vui lòng chọn 1 hoặc 2.")
                continue
            
            final_price = calculate_ticket_price(quantity, ticket_class)
            
            if ticket_class == 1:
                unit_display = BASE_PRICE
                class_name = "Economy"
            else:
                unit_display = BASE_PRICE * 1.5
                class_name = "Business"
            
            subtotal = unit_display * quantity
            service_fee = subtotal * 0.05
            
            print("-> Xác nhận đặt chỗ:")
            print(f"Số lượng: {quantity} | Hạng: {class_name}")
            print(f"Tạm tính: ${subtotal:,.2f}")
            print(f"Phí dịch vụ (5%): ${service_fee:,.2f}")
            print(f"Tổng thanh toán: ${final_price:,.2f}")
            
            process_booking(quantity, final_price)
            print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")
        
        elif choice == '2':
            print("--- HỦY VÉ & HOÀN TIỀN ---")
            
            try:
                refund_qty = int(input("Nhập số lượng vé muốn hủy: "))
            except ValueError:
                print("Đầu vào không hợp lệ.")
                continue
            
            if refund_qty <= 0:
                print("Số tiền không hợp lệ")
                continue
            potential_seats = available_seats + refund_qty
            if potential_seats > 50:
                print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
                continue
            
            refund_amount = process_refund(refund_qty)
            print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund_amount:,.2f} (80% giá cơ bản).")
            print(f"Ghế trống hiện tại: {available_seats}")
        
        elif choice == '3':
            display_flight_status()
        
        elif choice == '4':
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break
        
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()