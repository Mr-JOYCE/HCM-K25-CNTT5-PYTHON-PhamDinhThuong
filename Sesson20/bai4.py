import logging
import sys

logging.basicConfig(
    filename='roster_app.log',
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

roster = [
    {"player_id": "P01", "name": "Faker", "role": "Mid Lane", "salary": 5000.0, "status": "Active"},
    {"player_id": "P02", "name": "Oner", "role": "Jungle", "salary": 3500.0, "status": "Active"},
    {"player_id": "P03", "name": "Ruler", "role": "ADC", "salary": 6000.0, "status": "Benched"}
]

def calculate_actual_pay(player_dict):
    """Tính toán mức lương thực nhận dựa trên trạng thái thi đấu."""
    salary = float(player_dict['salary'])
    status = player_dict.get('status', 'Unknown')
    
    if status == 'Benched':
        return salary * 0.5
    return salary

def display_roster(roster_list):
    """Hiển thị danh sách đội hình thi đấu hiện tại."""
    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    if not roster_list:
        print("Đội hình hiện đang trống.")
        logging.info("Coach viewed an empty team roster.")
        return

    print(f"{'ID':<8} | {'Tên tuyển thủ':<20} | {'Vị trí':<15} | {'Lương':<12} | {'Trạng thái'}")
    print("-" * 80)
    for player in roster_list:
        try:
            status = player.get('status', 'Unknown')
            name_display = f"{player['name']} [DỰ BỊ]" if status == "Benched" else player['name']
            salary_display = f"{player['salary']:,.1f}"
            print(f"{player['player_id']:<8} | {name_display:<20} | {player['role']:<15} | {salary_display:<12} | {status}")
        except KeyError as e:
            logging.error(f"Missing key in roster data: {e}")
            print(f"Lỗi hiển thị dữ liệu cho mã tuyển thủ {player.get('player_id', 'Unknown')}")
    
    logging.info("Coach viewed the team roster.")

def sign_player(roster_list):
    """Chiêu mộ tuyển thủ mới vào đội hình."""
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    
    if not player_id:
        print("\nMã tuyển thủ không được để trống.")
        return

    if any(p['player_id'] == player_id for p in roster_list):
        print(f"\nLỗi: Mã tuyển thủ {player_id} đã tồn tại.")
        logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
        return

    name = input("Nhập tên tuyển thủ: ").strip()
    role = input("Nhập vị trí thi đấu: ").strip()

    while True:
        try:
            salary_input = float(input("Nhập mức lương hàng tháng: "))
            if salary_input <= 0:
                print("\nLương phải là số dương. Vui lòng nhập lại.")
                continue
            salary = salary_input
            break
        except ValueError:
            print("\nLương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")

    new_player = {
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    }
    roster_list.append(new_player)
    print(f"\nThành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(f"Signed new player {name} with salary {salary}")

def update_player_status(roster_list):
    """Cập nhật thông tin lương hoặc trạng thái thi đấu của tuyển thủ."""
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()
    
    target_player = next((p for p in roster_list if p['player_id'] == player_id), None)
    
    if not target_player:
        print(f"\nKhông tìm thấy tuyển thủ mang mã {player_id}.")
        logging.warning(f"Failed to update player - Player ID {player_id} not found")
        return

    try:
        print(f"\nTuyển thủ: {target_player['name']}")
        print(f"Vị trí: {target_player['role']}")
        print(f"Lương hiện tại: {target_player['salary']:,.1f}")
        print(f"Trạng thái hiện tại: {target_player['status']}")
    except KeyError as e:
        logging.error(f"Missing key when accessing player {player_id}: {e}")
        return

    print("\nBạn muốn cập nhật:")
    print("1. Cập nhật lương")
    print("2. Cập nhật trạng thái thi đấu")
    choice = input("Chọn chức năng cập nhật (1-2): ").strip()

    if choice == '1':
        while True:
            try:
                new_salary = float(input("Nhập mức lương mới: "))
                if new_salary <= 0:
                    print("\nLương phải là số dương. Vui lòng nhập lại.")
                    continue
                old_salary = target_player['salary']
                target_player['salary'] = new_salary
                print(f"\nThành công: Đã cập nhật lương cho tuyển thủ {player_id}.")
                logging.info(f"Updated player {player_id} salary from {old_salary} to {new_salary}")
                break
            except ValueError:
                print("\nLương phải là số. Vui lòng nhập lại.")
    elif choice == '2':
        print("\nChọn trạng thái mới:")
        print("1. Active")
        print("2. Benched")
        status_choice = input("Nhập lựa chọn trạng thái (1-2): ").strip()
        
        if status_choice == '1':
            target_player['status'] = "Active"
            print(f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.")
            logging.info(f"Updated player {player_id} status to Active")
        elif status_choice == '2':
            target_player['status'] = "Benched"
            print(f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.")
            logging.info(f"Updated player {player_id} status to Benched")
        else:
            print("\nLựa chọn không hợp lệ.")
    else:
        print("\nLựa chọn không hợp lệ.")

def generate_payroll_report(roster_list):
    """Tính toán và xuất báo cáo quỹ lương hàng tháng."""
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")
    
    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return

    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Trạng thái':<10} | {'Lương gốc':<12} | {'Lương thực nhận'}")
    print("-" * 80)
    
    total_payroll = 0.0
    
    for player in roster_list:
        try:
            actual_pay = calculate_actual_pay(player)
            total_payroll += actual_pay
            
            salary_str = f"{player['salary']:,.1f}"
            actual_pay_str = f"{actual_pay:,.1f}"
            
            print(f"{player['player_id']:<8} | {player['name']:<15} | {player.get('status', 'Unknown'):<10} | {salary_str:<12} | {actual_pay_str}")
        except KeyError as e:
            print(f"Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
            logging.error(f"Missing key while generating payroll report: {e}")
            print("-" * 80)
            print("Tổng quỹ lương hàng tháng: 0.0")
            return
            
    print("-" * 80)
    print(f"Tổng quỹ lương hàng tháng: {total_payroll:,.1f}")
    logging.info(f"Generated monthly payroll report. Total: {total_payroll}")

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == '1':
            display_roster(roster)
        elif choice == '2':
            sign_player(roster)
        elif choice == '3':
            update_player_status(roster)
        elif choice == '4':
            generate_payroll_report(roster)
        elif choice == '5':
            print("\nĐang thoát hệ thống. Tạm biệt!")
            logging.info("System closed.")
            sys.exit()
        else:
            print("\nLựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()