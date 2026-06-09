blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]

def find_bag_index(inventory, bag_id):
    if not bag_id:
        return -1
    
    search_id = bag_id.strip().upper()
    
    for index, bag in enumerate(inventory):
        if bag.startswith(search_id + "-"):
            return index
    
    return -1


def extract_bag_info(bag_string):
    return bag_string.split("-")


def validate_volume(volume_input):
    if not volume_input.strip().isdigit():
        return -1
    value = int(volume_input.strip())
    return value if value > 0 else -1

def display_inventory(inventory):
    print("\n--- DANH SÁCH KHO MÁU ---")
    print("Mã Túi | Người Hiến       | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    print("--------------------------------------------------------------")
    
    if not inventory:
        print("Kho máu hiện chưa có túi máu nào.")
        return
    
    total_volume = 0
    
    for bag in inventory:
        parts = extract_bag_info(bag)
        ma_tui = parts[0]
        nguoi_hien = parts[1]
        nhom_mau = parts[2]
        the_tich = int(parts[3])
        ngay_het_han = parts[4]
        
        total_volume += the_tich
        
        print(f"{ma_tui:<6} | {nguoi_hien:<15} | {nhom_mau:<7} | {the_tich} ml   | {ngay_het_han}")
    
    print("--------------------------------------------------------------")
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")

def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")
    
    ma_tui = input("Nhập mã túi máu mới: ").strip()
    
    if not ma_tui:
        print("Lỗi: Mã túi máu không được để trống!")
        return
    
    ma_tui = ma_tui.upper()
    
    if find_bag_index(inventory, ma_tui) != -1:
        print(f"Lỗi: Mã túi máu {ma_tui} đã tồn tại! Vui lòng nhập mã khác.")
        return
    
    ten_nguoi = input("Nhập tên người hiến: ").strip()
    
    if not ten_nguoi:
        print("Lỗi: Tên người hiến không được để trống!")
        return
    
    ten_nguoi = ten_nguoi.title()
    
    nhom_mau = input("Nhập nhóm máu: ").strip().upper()
    
    while True:
        the_tich = input("Nhập thể tích (ml): ").strip()
        the_tich_value = validate_volume(the_tich)
        
        if the_tich_value == -1:
            print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
        else:
            break
    
    ngay_het_han = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()
    
    new_bag = f"{ma_tui}-{ten_nguoi}-{nhom_mau}-{the_tich_value}-{ngay_het_han}"
    inventory.append(new_bag)
    
    print(f"Thành công: Đã nhập túi máu {ma_tui} vào kho!")


def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")
    
    ma_tui = input("Nhập mã túi máu cần cập nhật: ").strip()
    
    if not ma_tui:
        print("Lỗi: Mã túi máu không được để trống!")
        return
    
    ma_tui = ma_tui.upper()
    index = find_bag_index(inventory, ma_tui)
    
    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {ma_tui} trong kho!")
        return
    
    ngay_moi = input("Nhập ngày hết hạn mới: ").strip()
    
    if not ngay_moi:
        print("Lỗi: Ngày hết hạn không được để trống!")
        return
    
    parts = extract_bag_info(inventory[index])
    parts[4] = ngay_moi
    new_bag = "-".join(parts)
    inventory[index] = new_bag
    
    print(f"Thành công: Đã cập nhật ngày hết hạn cho túi máu {ma_tui}!")


def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")
    
    ma_tui = input("Nhập mã túi máu cần xuất/hủy: ").strip()
    
    if not ma_tui:
        print("Lỗi: Mã túi máu không được để trống!")
        return
    
    ma_tui = ma_tui.upper()
    index = find_bag_index(inventory, ma_tui)
    
    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {ma_tui} trong kho!")
        return
    
    inventory.pop(index)
    
    print(f"Thành công: Đã xuất túi máu {ma_tui} khỏi kho!")

def main():
    local_inventory = blood_inventory
    
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")
        
        try:
            chon = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
            continue
        
        if chon == 1:
            display_inventory(local_inventory)
        elif chon == 2:
            add_blood_bag(local_inventory)
        elif chon == 3:
            update_expiry(local_inventory)
        elif chon == 4:
            remove_blood_bag(local_inventory)
        elif chon == 5:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


if __name__ == "__main__":
    main()