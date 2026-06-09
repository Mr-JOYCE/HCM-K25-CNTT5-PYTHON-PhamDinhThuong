patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def validate_gender(gender_input):
    cleaned = gender_input.strip().lower()
    return cleaned == "nam" or cleaned == "nu"


def find_patient_index(patient_list, patient_id):
    if not patient_id:
        return -1
    
    search_id = patient_id.strip().upper()
    
    for index, patient in enumerate(patient_list):
        if patient[0].upper() == search_id:
            return index
    
    return -1

def display_patients(patient_list):
    print("\n----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
    
    for index, patient in enumerate(patient_list, 1):
        print(f"{index}. Mã: {patient[0]} | Tên: {patient[1]:<20} | Giới tính: {patient[2]:<3} | Bệnh: {patient[3]}")


def add_patient(patient_list):
    print("\n----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    
    ma_bn = input("Nhập mã bệnh nhân: ").strip()
    
    if not ma_bn:
        print("Mã bệnh nhân không được để trống!")
        return
    
    ma_bn_normalized = ma_bn.upper()
    
    if find_patient_index(patient_list, ma_bn_normalized) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return
    
    ten_bn = input("Nhập tên bệnh nhân: ").strip()
    
    if not ten_bn:
        print("Tên bệnh nhân không được để trống!")
        return
    
    ten_bn_normalized = ten_bn.title()
    while True:
        gioi_tinh = input("Nhập giới tính Nam/Nu: ")
        
        if not gioi_tinh.strip():
            print("Giới tính không được để trống!")
            continue
        
        if validate_gender(gioi_tinh):
            gioi_tinh_normalized = gioi_tinh.strip().title()
            break
        else:
            print("Giới tính không hợp lệ, vui lòng nhập lại!")
    
    chan_doan = input("Nhập chẩn đoán bệnh: ").strip()
    
    if not chan_doan:
        print("Chẩn đoán bệnh không được để trống!")
        return
    
    chan_doan_normalized = chan_doan.capitalize()
    new_patient = [ma_bn_normalized, ten_bn_normalized, gioi_tinh_normalized, chan_doan_normalized]
    patient_list.append(new_patient)
    
    print("Tiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list):
    print("\n----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    
    ma_bn = input("Nhập mã bệnh nhân cần cập nhật: ")
    
    if not ma_bn.strip():
        print("Mã bệnh nhân không được để trống!")
        return
    
    index = find_patient_index(patient_list, ma_bn)
    
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {ma_bn.upper()}!")
        return
    
    patient = patient_list[index]
    print(f"Tìm thấy bệnh nhân: {patient[1]}")
    print(f"Chẩn đoán hiện tại: {patient[3]}")
    
    chan_doan_moi = input("Nhập chẩn đoán mới: ").strip()
    
    if not chan_doan_moi:
        print("Chẩn đoán bệnh không được để trống!")
        return
    
    patient_list[index][3] = chan_doan_moi.capitalize()
    
    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
    print("\n----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    
    tu_khoa = input("Nhập từ khóa tên bệnh: ").strip()
    
    if not tu_khoa:
        print("Từ khóa tìm kiếm không được để trống!")
        return
    
    tu_khoa_lower = tu_khoa.lower()
    ket_qua = []
    
    for patient in patient_list:
        benh = patient[3].lower()
        if tu_khoa_lower in benh:
            ket_qua.append(patient)
    
    if not ket_qua:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
    else:
        print("Kết quả tìm kiếm:")
        for index, patient in enumerate(ket_qua, 1):
            print(f"{index}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")
    
    print(f"Có tổng cộng {len(ket_qua)} bệnh nhân mắc bệnh liên quan đến '{tu_khoa}'.")

def main():
    local_patients = patients  
    
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")
        
        try:
            chon = int(input("Nhập lựa chọn của bạn: "))
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
            continue
        
        if chon == 1:
            display_patients(local_patients)
        elif chon == 2:
            add_patient(local_patients)
        elif chon == 3:
            update_diagnosis(local_patients)
        elif chon == 4:
            search_by_disease(local_patients)
        elif chon == 5:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


if __name__ == "__main__":
    main()