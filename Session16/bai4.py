patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def normalize_dash(text):
    return text.replace('-', ' ')


def validate_year(year_str):
    if not year_str.isdigit():
        return -1
    
    year = int(year_str)
    import datetime
    current_year = datetime.datetime.now().year
    
    if year < 1900 or year > current_year:
        return -1
    
    return year


def find_patient_index(records, patient_id):
    normalized_id = patient_id.strip().upper()
    
    for index, record in enumerate(records):
        if record.startswith(normalized_id + "-"):
            return index
    
    return -1

def display_records(records):
    print("\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")
    
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return
    
    for index, record in enumerate(records, 1):
        parts = record.split('-')
        ma_bn = parts[0]
        ten_bn = parts[1]
        nam_sinh = parts[2]
        chan_doan = parts[3]
        
        print(f"{index}. [{ma_bn}] {ten_bn:<20} | Năm sinh: {nam_sinh} | Chẩn đoán: {chan_doan}")
    
    print("--------------------------------------------------------------------------")


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    
    ma_bn = input("Nhập mã bệnh nhân: ").strip()
    
    if not ma_bn:
        print("Mã bệnh nhân không được để trống!")
        return
    
    ma_bn_normalized = ma_bn.upper()
    
    if find_patient_index(records, ma_bn_normalized) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return
    
    ten_bn = input("Nhập tên bệnh nhân: ").strip()
    
    if not ten_bn:
        print("Tên bệnh nhân không được để trống!")
        return
    
    ten_bn_normalized = normalize_dash(ten_bn).title()
    
    while True:
        nam_sinh_input = input("Nhập năm sinh: ").strip()
        nam_sinh = validate_year(nam_sinh_input)
        
        if nam_sinh == -1:
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        else:
            break
    
    chan_doan = input("Nhập chẩn đoán: ").strip()
    
    if not chan_doan:
        print("Chẩn đoán không được để trống!")
        return
    
    chan_doan_normalized = normalize_dash(chan_doan).capitalize()
    
    new_record = f"{ma_bn_normalized}-{ten_bn_normalized}-{nam_sinh}-{chan_doan_normalized}"
    
    records.append(new_record)
    
    print("Thêm hồ sơ bệnh nhân thành công!")


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    
    ma_bn = input("Nhập mã bệnh nhân cần cập nhật: ").strip()
    
    if not ma_bn:
        print("Mã bệnh nhân không được để trống!")
        return
    
    index = find_patient_index(records, ma_bn)
    
    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {ma_bn.upper()}!")
        return
    
    current_record = records[index]
    parts = current_record.split('-')
    
    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")
    
    chan_doan_moi = input("Nhập chẩn đoán mới: ").strip()
    
    if not chan_doan_moi:
        print("Chẩn đoán không được để trống!")
        return
    
    chan_doan_moi_normalized = normalize_dash(chan_doan_moi).capitalize()
    
    parts[3] = chan_doan_moi_normalized
    new_record = "-".join(parts)
    
    records[index] = new_record
    
    print("Cập nhật chẩn đoán thành công!")


def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    
    import datetime
    current_year = datetime.datetime.now().year
    
    tre_em = 0
    truong_thanh = 0
    cao_tuoi = 0
    
    for record in records:
        parts = record.split('-')
        nam_sinh = int(parts[2])
        tuoi = current_year - nam_sinh
        
        if tuoi < 16:
            tre_em += 1
        elif tuoi <= 60:
            truong_thanh += 1
        else:
            cao_tuoi += 1
    
    print(f"Trẻ em: {tre_em} bệnh nhân")
    print(f"Trưởng thành: {truong_thanh} bệnh nhân")
    print(f"Người cao tuổi: {cao_tuoi} bệnh nhân")
    print("--------------------------------------")

def main():
    local_records = patient_records
    
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("==================================================")
        
        try:
            chon = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
            continue
        
        if chon == 1:
            display_records(local_records)
        elif chon == 2:
            add_patient(local_records)
        elif chon == 3:
            update_diagnosis(local_records)
        elif chon == 4:
            generate_age_report(local_records)
        elif chon == 5:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


if __name__ == "__main__":
    main()