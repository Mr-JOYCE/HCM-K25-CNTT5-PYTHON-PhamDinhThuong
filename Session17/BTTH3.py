teams_list = []
match_schedule = [] 

def combinations_custom(iterable, r):
    pool = list(iterable)
    n = len(pool)
    
    if r > n or r <= 0:
        return []
    
    indices = list(range(r))
    result = [tuple(pool[i] for i in indices)]
    
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return result
        
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        
        result.append(tuple(pool[i] for i in indices))

def nhap_doi_tuyen():
    global teams_list
    
    print("\n--- NHẬP DANH SÁCH ---")
    raw_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ")
    temp_list = [team.strip().upper() for team in raw_input.split(',')]
    teams_list = list(dict.fromkeys(temp_list))
    
    if len(temp_list) != len(teams_list):
        print(f"Đã loại bỏ {len(temp_list) - len(teams_list)} đội trùng lặp.")
    
    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")

def tao_lich_thi_dau():
    global match_schedule
    
    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    
    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return
    
    pairs = combinations_custom(teams_list, 2)
    
    match_schedule = [f"{pair[0]} vs {pair[1]}" for pair in pairs]
    
    for idx, match in enumerate(match_schedule, 1):
        print(f"{idx}. {match}")
    
    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")

def tao_ma_tran_dau():
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    
    if not match_schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return
    
    for idx, match in enumerate(match_schedule, 1):
        teams = match.split(' vs ')
        team_a = teams[0]
        team_b = teams[1]
        
        prefix_a = (team_a + "XXX")[:3]  
        prefix_b = (team_b + "XXX")[:3]
        
        match_index = f"{idx:02d}"
        print(f"Trận {idx} ({match}) -> ID: M{match_index}-{prefix_a}-{prefix_b}")

def main():
    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
        print("4. Đóng hệ thống")
        print("==============================================")
        
        try:
            chon = int(input("Chọn chức năng (1-4): "))
        except ValueError:
            print("Vui lòng nhập số!")
            continue
        
        if chon == 1:
            nhap_doi_tuyen()
        elif chon == 2:
            tao_lich_thi_dau()
        elif chon == 3:
            tao_ma_tran_dau()
        elif chon == 4:
            print("Cảm ơn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Chức năng không hợp lệ!")

if __name__ == "__main__":
    main()