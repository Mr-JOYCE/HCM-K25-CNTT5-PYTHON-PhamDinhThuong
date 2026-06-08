atm_vault_balance = 50000000 
user_account_balance = 10000000  

def display_balances():
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    global atm_vault_balance, user_account_balance
    
    atm_vault_balance += amount
    user_account_balance += amount
    
    return True


def check_withdrawal_rules(amount):
    fee = 1100
    total_deduction = amount + fee
    
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
        
    return "OK"


def execute_withdrawal(total_deduction, amount_to_dispense):
    global atm_vault_balance, user_account_balance
    
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    
    print(f"Giao dịch đang xử lý...")
    print(f"Phí giao dịch: {1100:,} VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")

def main():
    global atm_vault_balance, user_account_balance
    
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")
        
        try:
            choice = input("Vui lòng chọn giao dịch (1-4): ")
        except EOFError:
            break
            
        if choice == '1':
            display_balances()
            
        elif choice == '2':
            print("--- NẠP TIỀN ---")
            try:
                amount = int(input("Nhập số tiền muốn nạp: "))
            except ValueError:
                print("Đầu vào không hợp lệ.")
                continue
                
            if amount <= 0:
                print("Số tiền không hợp lệ")
                continue
                
            success = deposit_money(amount)
            if success:
                print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
                
        elif choice == '3':
            print("--- RÚT TIỀN ---")
            try:
                amount = int(input("Nhập số tiền cần rút: "))
            except ValueError:
                print("Đầu vào không hợp lệ.")
                continue
            
            if amount <= 0:
                print("Số tiền không hợp lệ")
                continue
                
            if amount % 50000 != 0:
                print("Số tiền rút phải là bội số của 50,000")
                continue
                
            status = check_withdrawal_rules(amount)
            
            if status == "OK":
                total_deduction = amount + 1100
                execute_withdrawal(total_deduction, amount)
            elif status == "ATM_OUT_OF_CASH":
                print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
            elif status == "INSUFFICIENT_FUNDS":
                print("Giao dịch thất bại: Tài khoản không đủ tiền.")
                
        elif choice == '4':
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break
            
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()