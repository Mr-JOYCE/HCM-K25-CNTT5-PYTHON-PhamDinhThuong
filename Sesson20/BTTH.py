import logging

logging.basicConfig(
    filename="arena_tickets.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

ticket_db = [
    {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
    {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
    {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
]

def display_tickets(tickets):
    if not tickets:
        print("Hiện chưa có vé nào trong hệ thống.")
        return
    print("\n--- DANH SÁCH VÉ ---")
    print("Mã Vé | Tên Khách Hàng | Giá Vé | Chỗ Ngồi | Trạng Thái")
    print("-" * 60)
    try:
        for t in tickets:
            seat = f"{t['seat'][0]}-{t['seat'][1]}"
            status = t["status"]
            if status == "Cancelled":
                status += " [ĐÃ HỦY]"
            print(f"{t['ticket_id']} | {t['buyer_name']} | {t['price']} | {seat} | {status}")
        logging.info("User viewed ticket list.")
    except KeyError as e:
        print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
        logging.error(f"Missing key while displaying ticket: {e}")
    print("-" * 60)


def book_ticket(tickets):
    print("\n--- ĐẶT VÉ MỚI ---")
    ticket_id = input("Nhập mã vé: ")
    for t in tickets:
        if t["ticket_id"] == ticket_id:
            print(f"Lỗi: Mã vé {ticket_id} đã tồn tại.")
            logging.warning(f"Duplicate ticket ID entered: {ticket_id}")
            return
    buyer_name = input("Nhập tên khách hàng: ")

    while True:
        try:
            price = float(input("Nhập giá vé: "))
            if price <= 0:
                print("Giá vé phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Giá vé phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")

    row = input("Nhập khu vực ghế: ")
    while True:
        try:
            seat_number = int(input("Nhập số ghế: "))
            break
        except ValueError:
            print("Số ghế phải là số nguyên. Vui lòng nhập lại.")

    new_ticket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": (row, seat_number)
    }
    tickets.append(new_ticket)
    print(f"Thành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")


def change_seat(tickets):
    print("\n--- ĐỔI CHỖ NGỒI ---")
    ticket_id = input("Nhập mã vé cần đổi chỗ: ")
    for t in tickets:
        if t["ticket_id"] == ticket_id:
            new_row = input("Nhập khu vực ghế mới: ")
            while True:
                try:
                    new_number = int(input("Nhập số ghế mới: "))
                    break
                except ValueError:
                    print("Số ghế phải là số nguyên. Vui lòng nhập lại.")
            t["seat"] = (new_row, new_number)
            print(f"Thành công: Đã đổi chỗ vé {ticket_id} sang {new_row}-{new_number}.")
            logging.info(f"Seat changed for ticket {ticket_id} to {new_row}-{new_number}")
            return
    print(f"Không tìm thấy vé mang mã {ticket_id}.")
    logging.warning(f"Change seat failed - Ticket {ticket_id} not found")


def cancel_ticket(tickets):
    print("\n--- HỦY VÉ ---")
    ticket_id = input("Nhập mã vé cần hủy: ")
    for t in tickets:
        if t["ticket_id"] == ticket_id:
            if t["status"] == "Cancelled":
                print(f"Vé {ticket_id} đã ở trạng thái Cancelled trước đó.")
                return
            t["status"] = "Cancelled"
            print(f"Thành công: Vé {ticket_id} đã được hủy.")
            logging.warning(f"Ticket {ticket_id} has been cancelled.")
            return
    print(f"Không tìm thấy vé mang mã {ticket_id}.")
    logging.warning(f"Cancel ticket failed - Ticket {ticket_id} not found")


def calculate_revenue(tickets):
    print("\n--- BÁO CÁO DOANH THU ---")
    booked_count = sum(1 for t in tickets if t.get("status") == "Booked")
    cancelled_count = sum(1 for t in tickets if t.get("status") == "Cancelled")
    total = 0.0
    try:
        for t in tickets:
            if t["status"] == "Booked":
                total += t["price"]
    except KeyError as e:
        print("Lỗi: Một vé đang bị thiếu dữ liệu doanh thu.")
        logging.error(f"Missing key while calculating revenue: {e}")
    print(f"Tổng số vé đã đặt: {booked_count}")
    print(f"Tổng số vé đã hủy: {cancelled_count}")
    print(f"Tổng doanh thu hợp lệ: {total}")
    logging.info(f"Revenue report generated. Total: {total}")

if __name__ == "__main__":
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===")
        print("1. Xem danh sách vé đã bán")
        print("2. Đặt vé mới")
        print("3. Đổi chỗ ngồi (Cập nhật vé)")
        print("4. Hủy vé")
        print("5. Báo cáo doanh thu")
        print("6. Thoát chương trình")
        print("========================================")
        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            display_tickets(ticket_db)
        elif choice == "2":
            book_ticket(ticket_db)
        elif choice == "3":
            change_seat(ticket_db)
        elif choice == "4":
            cancel_ticket(ticket_db)
        elif choice == "5":
            calculate_revenue(ticket_db)
        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý vé Rikkei Esports.")
            logging.info("Ticket management system closed.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1-6.")
