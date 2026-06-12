import logging
import sys

logging.basicConfig(
    filename='fantasy_league.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

players = [
    {
        "player_id": "T101",
        "name": "Faker",
        "market_value": 5000,
        "fan_tokens": 1500,
        "match_points": 0,
        "form_multiplier": 1.0
    },
    {
        "player_id": "GEN01",
        "name": "Chovy",
        "market_value": 4800,
        "fan_tokens": 800,
        "match_points": 500,
        "form_multiplier": 1.2
    },
    {
        "player_id": "DRX01",
        "name": "Deft",
        "market_value": 3000,
        "fan_tokens": 0,
        "match_points": 0,
        "form_multiplier": 0.8
    }
]

def find_player_by_id(players_list: list, player_id: str) -> int:
    formatted_id = player_id.strip().upper()
    for index, player in enumerate(players_list):
        if player.get("player_id", "").strip().upper() == formatted_id:
            return index
    return -1

def calc_actual_withdrawal(withdraw_amount: int) -> float:
    if withdraw_amount < 0:
        raise ValueError("Số lượng rút không được là số âm.")
    return float(withdraw_amount) * 0.9

def display_market(players_list: list) -> None:
    print("\n--- SÀN GIAO DỊCH TUYỂN THỦ ---")
    if not players_list:
        print("Sàn giao dịch hiện chưa có tuyển thủ nào.")
        return

    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Giá trị thị trường':<20} | {'Fan Token':<10} | {'Điểm trận':<10} | {'Hệ số':<6} | {'Trạng thái đầu tư'}")
    print("-" * 105)

    for player in players_list:
        p_id = player.get("player_id", "Unknown")
        name = player.get("name", "Unknown")
        market_value = player.get("market_value", 0)
        fan_tokens = player.get("fan_tokens", 0)
        match_points = player.get("match_points", 0)
        form_multiplier = player.get("form_multiplier", 1.0)

        if fan_tokens == 0:
            status = "Chưa có người đầu tư"
        elif 0 < fan_tokens <= 1000:
            status = "Đang thu hút"
        else:
            status = "Tuyển thủ Hot"

        print(f"{p_id:<8} | {name:<15} | {market_value:<20,} | {fan_tokens:<10,} | {match_points:<10,} | {form_multiplier:<6.1f} | {status}")
    
    logging.info("User viewed the player market.")

def invest_tokens(players_list: list) -> None:
    print("\n--- ĐẦU TƯ FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ")
    idx = find_player_by_id(players_list, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Invest failed - Player {player_id.strip().upper()} not found")
        return

    while True:
        try:
            tokens = int(input("Nhập số token muốn đầu tư: "))
            if tokens <= 0:
                print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
            logging.warning("Invalid token input while investing")

    target_player = players_list[idx]
    current_tokens = target_player.get("fan_tokens", 0)
    target_player["fan_tokens"] = current_tokens + tokens

    print(f"\nThành công: Đã đầu tư {tokens} token vào tuyển thủ {target_player.get('player_id')}.")
    print(f"Số Fan Token hiện tại của {target_player.get('name')}: {target_player.get('fan_tokens'):,}")
    logging.info(f"Invested {tokens} tokens into {target_player.get('player_id')}")

def withdraw_tokens(players_list: list) -> None:
    print("\n--- RÚT VỐN FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ")
    idx = find_player_by_id(players_list, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Withdraw failed - Player {player_id.strip().upper()} not found")
        return

    target_player = players_list[idx]
    current_tokens = target_player.get("fan_tokens", 0)

    while True:
        try:
            tokens_to_withdraw = int(input("Nhập số token muốn rút: "))
            if tokens_to_withdraw <= 0:
                print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
            logging.warning("Invalid token input while withdrawing")

    if tokens_to_withdraw > current_tokens:
        print("\nKhông thể rút. Số token muốn rút vượt quá số Fan Token hiện có.")
        print(f"Fan Token hiện có của {target_player.get('name')}: {current_tokens:,}")
        logging.warning("Withdraw failed - Amount exceeds current fan tokens")
        return

    actual_received = calc_actual_withdrawal(tokens_to_withdraw)
    fee = float(tokens_to_withdraw) - actual_received
    target_player["fan_tokens"] = current_tokens - tokens_to_withdraw

    print(f"\nThành công: Đã rút {tokens_to_withdraw} token khỏi tuyển thủ {target_player.get('player_id')}.")
    print(f"Phí giao dịch 10%: {fee} token")
    print(f"Số token thực nhận về ví: {actual_received} token")
    print(f"Fan Token còn lại của {target_player.get('name')}: {target_player.get('fan_tokens'):,}")
    logging.info(f"Withdrawn {tokens_to_withdraw} tokens from {target_player.get('player_id')}. Actual received: {actual_received}")

def update_form(players_list: list) -> None:
    print("\n--- CẬP NHẬT HỆ SỐ PHONG ĐỘ ---")
    player_id = input("Nhập mã tuyển thủ: ")
    idx = find_player_by_id(players_list, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Update form failed - Player {player_id.strip().upper()} not found")
        return

    target_player = players_list[idx]

    while True:
        try:
            new_form = float(input("Nhập hệ số phong độ mới (0.5 - 2.5): "))
            if new_form < 0.5 or new_form > 2.5:
                print("\nHệ số phong độ chỉ được nằm trong khoảng 0.5 đến 2.5.")
                continue
            break
        except ValueError:
            print("\nHệ số phong độ phải là số thực. Vui lòng nhập lại.")

    target_player["form_multiplier"] = new_form
    print(f"\nThành công: Đã cập nhật hệ số phong độ cho {target_player.get('name')}.")
    print(f"Hệ số mới: x{new_form}")
    logging.info(f"Updated form multiplier for {target_player.get('player_id')} to {new_form}")

def calculate_match_points(players_list: list) -> None:
    print("\n--- CHẤM ĐIỂM SAU TRẬN ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ: ")
    idx = find_player_by_id(players_list, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        return

    target_player = players_list[idx]

    while True:
        try:
            base_points = float(input("Nhập điểm gốc của trận đấu: "))
            break
        except ValueError:
            print("\nĐiểm gốc phải là số. Vui lòng nhập lại.")

    form_multiplier = target_player.get("form_multiplier", 1.0)
    actual_points = base_points * form_multiplier
    current_match_points = target_player.get("match_points", 0)
    target_player["match_points"] = current_match_points + actual_points

    print(f"\n>> Tuyển thủ {target_player.get('name')} nhận được {actual_points} điểm (Hệ số x{form_multiplier}).")
    print(f"Tổng điểm: {target_player.get('match_points')}")
    logging.info(f"Added {actual_points} match points to {target_player.get('player_id')}")

def main() -> None:
    while True:
        print("\n===== HỆ THỐNG RIKKEI ESPORTS FANTASY =====")
        print("1. Xem Sàn Giao Dịch Tuyển Thủ")
        print("2. Đầu tư Fan Token")
        print("3. Rút vốn (Hoàn trả Token)")
        print("4. Biến động phong độ (Cập nhật hệ số)")
        print("5. Chấm điểm sau trận đấu")
        print("6. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == '1':
            display_market(players)
        elif choice == '2':
            invest_tokens(players)
        elif choice == '3':
            withdraw_tokens(players)
        elif choice == '4':
            update_form(players)
        elif choice == '5':
            calculate_match_points(players)
        elif choice == '6':
            print("\nĐóng hệ thống Rikkei Esports Fantasy.")
            logging.info("System closed.")
            sys.exit()
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()