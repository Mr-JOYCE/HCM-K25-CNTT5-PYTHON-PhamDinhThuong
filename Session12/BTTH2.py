"""
Savings Account Management CLI for TechBank.

Data structure: list of dicts where each dict contains:
{ account_id, customer_name, balance, term_months, interest_rate, status }

This module implements a command-line interface to view, add, update,
close accounts, compute maturity interest, and check early withdrawal.

All user-facing messages follow the requirements and handle edge cases.
"""

saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]


def normalize_account_id(acc_id: str) -> str:
    return "".join(acc_id.split()).upper()


def find_account(acc_id: str):
    for acc in saving_accounts:
        if acc["account_id"] == acc_id:
            return acc
    return None


def list_accounts():
    if not saving_accounts:
        print("Danh sách sổ tiết kiệm hiện đang trống")
        return

    print("Danh sách sổ tiết kiệm:")
    for i, acc in enumerate(saving_accounts, start=1):
        print(f"{i}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")


def add_account():
    raw_id = input("Nhập mã sổ tiết kiệm: ")
    acc_id = normalize_account_id(raw_id)
    if not acc_id:
        print("Mã sổ tiết kiệm không hợp lệ!")
        return

    if find_account(acc_id) is not None:
        print("Mã sổ tiết kiệm đã tồn tại!")
        return

    customer_name = input("Nhập tên khách hàng: ").strip()
    if not customer_name:
        print("Tên khách hàng không được để trống")
        return

    try:
        balance_raw = input("Nhập số tiền gửi: ")
        balance = int(balance_raw)
        term_raw = input("Nhập kỳ hạn gửi theo tháng: ")
        term_months = int(term_raw)
    except ValueError:
        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
        return

    if balance <= 0 or term_months <= 0:
        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
        return

    try:
        interest_raw = input("Nhập lãi suất năm: ")
        interest_rate = float(interest_raw)
    except ValueError:
        print("Lãi suất không hợp lệ!")
        return

    if interest_rate <= 0:
        print("Lãi suất không hợp lệ!")
        return

    new_acc = {
        "account_id": acc_id,
        "customer_name": customer_name,
        "balance": balance,
        "term_months": term_months,
        "interest_rate": interest_rate,
        "status": "active"
    }
    saving_accounts.append(new_acc)
    print("Mở sổ tiết kiệm thành công!")


def update_account():
    raw_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ")
    acc_id = normalize_account_id(raw_id)
    acc = find_account(acc_id)
    if acc is None:
        print("Không tìm thấy mã sổ tiết kiệm")
        return

    if acc.get("status") == "closed":
        print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
        return

    customer_name = input("Nhập tên khách hàng mới: ").strip()
    if not customer_name:
        print("Tên khách hàng không được để trống")
        return

    try:
        balance_raw = input("Nhập số tiền gửi mới: ")
        balance = int(balance_raw)
        term_raw = input("Nhập kỳ hạn mới theo tháng: ")
        term_months = int(term_raw)
    except ValueError:
        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
        return

    if balance <= 0 or term_months <= 0:
        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
        return

    try:
        interest_raw = input("Nhập lãi suất năm mới: ")
        interest_rate = float(interest_raw)
    except ValueError:
        print("Lãi suất không hợp lệ!")
        return

    if interest_rate <= 0:
        print("Lãi suất không hợp lệ!")
        return

    acc["customer_name"] = customer_name
    acc["balance"] = balance
    acc["term_months"] = term_months
    acc["interest_rate"] = interest_rate
    print("Cập nhật sổ tiết kiệm thành công!")


def close_account():
    raw_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ")
    acc_id = normalize_account_id(raw_id)
    acc = find_account(acc_id)
    if acc is None:
        print("Không tìm thấy mã sổ tiết kiệm")
        return

    acc["status"] = "closed"
    print("Tất toán sổ tiết kiệm thành công (trạng thái: closed)")


def calculate_maturity_interest():
    raw_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ")
    acc_id = normalize_account_id(raw_id)
    acc = find_account(acc_id)
    if acc is None:
        print("Không tìm thấy mã sổ tiết kiệm")
        return

    if acc.get("status") == "closed":
        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
        return

    balance = acc["balance"]
    rate = acc["interest_rate"]
    term = acc["term_months"]

    interest = balance * rate / 100.0 * term / 12.0
    total = balance + interest
    print(f"Tiền lãi dự kiến: {interest:.2f}")
    print(f"Tổng tiền nhận khi đến hạn: {total:.2f}")


def check_early_withdrawal():
    raw_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ")
    acc_id = normalize_account_id(raw_id)
    acc = find_account(acc_id)
    if acc is None:
        print("Không tìm thấy mã sổ tiết kiệm")
        return

    if acc.get("status") == "closed":
        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
        return

    try:
        months_raw = input("Nhập số tháng thực gửi: ")
        months_actual = int(months_raw)
    except ValueError:
        print("Số tháng thực gửi không hợp lệ!")
        return

    if months_actual <= 0:
        print("Số tháng thực gửi không hợp lệ!")
        return

    term = acc["term_months"]
    balance = acc["balance"]
    if months_actual < term:
        applied_rate = 0.5
        print("Rút trước hạn: áp dụng lãi suất 0.5%/năm")
    else:
        applied_rate = acc["interest_rate"]
        print("Đủ kỳ hạn hoặc đã hết kỳ hạn: áp dụng lãi suất gốc của sổ")

    interest = balance * applied_rate / 100.0 * months_actual / 12.0
    total = balance + interest
    print(f"Tiền lãi thực nhận: {interest:.2f}")
    print(f"Tổng tiền thực nhận: {total:.2f}")


def show_menu():
    print("===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")


def main():
    while True:
        show_menu()
        choice = input("Chọn chức năng (1-7): ")
        try:
            option = int(choice)
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")
            continue

        if option == 1:
            list_accounts()
        elif option == 2:
            add_account()
        elif option == 3:
            update_account()
        elif option == 4:
            close_account()
        elif option == 5:
            calculate_maturity_interest()
        elif option == 6:
            check_early_withdrawal()
        elif option == 7:
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")


if __name__ == "__main__":
    main()


