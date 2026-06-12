import logging
import unittest
import sys

logging.basicConfig(
    filename='tournament_app.log',
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

matches = [
    {"match_id": "M01", "team_a": "T1", "team_b": "GenG", "score_a": 2, "score_b": 1, "status": "Completed"},
    {"match_id": "M02", "team_a": "JDG", "team_b": "BLG", "score_a": 0, "score_b": 0, "status": "Pending"}
]

def display_matches(match_list):
    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        logging.info("User viewed the match list (empty).")
        return

    print(f"{'Mã trận':<10} | {'Đội A':<15} | {'Đội B':<15} | {'Tỷ số':<7} | {'Trạng thái'}")
    print("-" * 70)
    for match in match_list:
        try:
            score_str = f"{match['score_a']}-{match['score_b']}"
            print(f"{match['match_id']:<10} | {match['team_a']:<15} | {match['team_b']:<15} | {score_str:<7} | {match['status']}")
        except KeyError as e:
            logging.error(f"Missing key in match data: {e}")
            print(f"Lỗi: Dữ liệu trận đấu {match.get('match_id', 'Unknown')} bị thiếu thông tin.")
    
    logging.info("User viewed the match list.")

def add_match(match_list):
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")
    match_id = input("Nhập mã trận đấu: ").strip()
    
    if not match_id:
        print("\nMã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return

    if any(m['match_id'] == match_id for m in match_list):
        print(f"\nLỗi: Mã trận đấu {match_id} đã tồn tại.")
        logging.warning(f"Match ID {match_id} already exists.")
        return

    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if not team_a or not team_b:
        print("\nTên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
    match_list.append(new_match)
    print(f"\nThành công: Đã thêm trận đấu {match_id}.")
    logging.info(f"Match {match_id} added successfully")

def update_score(match_list):
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()
    
    target_match = next((m for m in match_list if m['match_id'] == match_id), None)
    
    if not target_match:
        print(f"\nKhông tìm thấy trận đấu mang mã {match_id}.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return

    try:
        print(f"\nTrận đấu: {target_match['team_a']} vs {target_match['team_b']} ({target_match['status']})")
    except KeyError as e:
        logging.error(f"Missing key when accessing match {match_id}: {e}")
        print("Lỗi dữ liệu hệ thống.")
        return

    def get_valid_score(team_name):
        while True:
            try:
                score = int(input(f"Nhập điểm {team_name}: "))
                if score < 0:
                    print("\nĐiểm số phải lớn hơn hoặc bằng 0.")
                    logging.error(f"Negative score input detected: {score}")
                    continue
                return score
            except ValueError as e:
                print("\nĐiểm số phải là số nguyên. Vui lòng nhập lại.")
                logging.error(f"Invalid score input. Error: {e}")

    score_a = get_valid_score("Đội A")
    score_b = get_valid_score("Đội B")

    if score_a == 0 and score_b == 0:
        confirm = input("\nTỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): ").strip().lower()
        if confirm == 'y':
            target_match['status'] = "Completed"
        else:
            target_match['status'] = "Pending"
    else:
        target_match['status'] = "Completed"

    target_match['score_a'] = score_a
    target_match['score_b'] = score_b

    print(f"\nThành công: Đã cập nhật tỷ số trận đấu {match_id}.")
    logging.info(f"Match {match_id} score updated successfully")

def determine_winner(match):
    try:
        if match['status'] == 'Pending':
            return "Not Started"
        
        if match['score_a'] > match['score_b']:
            return match['team_a']
        elif match['score_b'] > match['score_a']:
            return match['team_b']
        else:
            return "Draw"
    except KeyError as e:
        logging.error(f"KeyError in determine_winner: {e}")
        return "Error"

def generate_report(match_list):
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    completed_matches = [m for m in match_list if m.get('status') == "Completed"]
    
    if not completed_matches:
        print("Chưa có trận đấu nào hoàn thành.")
    else:
        for match in completed_matches:
            try:
                winner = determine_winner(match)
                print(f"{match['match_id']}: {match['team_a']} {match['score_a']}-{match['score_b']} {match['team_b']} | Kết quả: {winner}")
            except KeyError as e:
                logging.error(f"Data error in report generation: {e}")
    
    print(f"\nTổng số trận đã hoàn thành: {len(completed_matches)}")
    logging.info("User generated tournament report.")

def run_app():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == '1':
            display_matches(matches)
        elif choice == '2':
            add_match(matches)
        elif choice == '3':
            update_score(matches)
        elif choice == '4':
            generate_report(matches)
        elif choice == '5':
            print("\nĐang đóng hệ thống... Tạm biệt!")
            logging.info("System closed and program exited.")
            break
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")
            logging.warning("Invalid menu choice selected.")

class TestTournamentSystem(unittest.TestCase):
    
    def test_team_a_wins(self):
        match = {"match_id": "M01", "team_a": "T1", "team_b": "GenG", "score_a": 2, "score_b": 0, "status": "Completed"}
        self.assertEqual(determine_winner(match), "T1")

    def test_draw(self):
        match = {"match_id": "M02", "team_a": "JDG", "team_b": "BLG", "score_a": 1, "score_b": 1, "status": "Completed"}
        self.assertEqual(determine_winner(match), "Draw")

    def test_pending(self):
        match = {"match_id": "M03", "team_a": "G2", "team_b": "FNC", "score_a": 0, "score_b": 0, "status": "Pending"}
        self.assertEqual(determine_winner(match), "Not Started")
        
    def test_missing_keys(self):
        match = {"match_id": "M04", "team_a": "C9", "team_b": "FLY"}
        self.assertEqual(determine_winner(match), "Error")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        sys.argv.pop() 
        unittest.main()
    else:
        run_app()