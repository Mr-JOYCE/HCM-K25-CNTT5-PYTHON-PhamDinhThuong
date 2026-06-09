er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]

def find_patient_index(patients, er_id):
    if not er_id:
        return -1
    
    search_id = er_id.strip().upper()
    
    for index, patient in enumerate(patients):
        if patient.startswith(search_id + "|"):
            return index
    
    return -1


def extract_vital_value(vital_string):
    try:
        parts = vital_string.split(':')
        if len(parts) < 2:
            return -1
        
        value = float(parts[1])
        return value
    except (ValueError, IndexError):
        return -1


def validate_vital_hr(hr_input):
    cleaned = hr_input.strip()
    
    # Kiem tra co phai la so
    if not cleaned.isdigit():
        return -1
    
    value = int(cleaned)
    
    if value <= 0:
        return -1
    
    return value


def validate_vital_temp(temp_input):
    try:
        value = float(temp_input.strip())
        
        if value < 36.5:
            return -1
        
        return value
    except ValueError:
        return -1

def display_dashboard(patients):
    print("\n--- BẢNG THEO DÕI CA CẤP CỨU ------------------------------------")
    
    if not patients:
        print("Khoa cấp cứu hiện đang trống.")
        return
    
    for index, patient in enumerate(patients, 1):
        parts = patient.split('|')
        ma_er = parts[0]
        ten_bn = parts[1]
        hr_raw = parts[2]
        temp_raw = parts[3]
        
        hr_value = extract_vital_value(hr_raw)
        temp_value = extract_vital_value(temp_raw)
        
        print(f"{index}. [{ma_er}] {ten_bn:<20} | Nhịp tim: {hr_value} bpm | Nhiệt độ: {temp_value} °C")
    
    print("-----------------------------------------------------------------")


def admit_patient(patients):
    print("\n--- TIẾP NHẬN CA CẤP CỨU MỚI ---")
    
    ma_er = input("Nhập mã ER: ").strip()
    
    if not ma_er:
        print("Mã ER không được để trống!")
        return
    
    ma_er_normalized = ma_er.upper()
    
    if find_patient_index(patients, ma_er_normalized) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return
    
    ten_bn = input("Nhập tên bệnh nhân: ").strip()
    
    if not ten_bn:
        print("Tên bệnh nhân không được để trống!")
        return
    
    ten_bn_normalized = ten_bn.title()
    
    while True:
        hr_input = input("Nhập nhịp tim HR: ").strip()
        hr_value = validate_vital_hr(hr_input)
        
        if hr_value == -1:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
        else:
            break

    while True:
        temp_input = input("Nhập nhiệt độ TEMP: ").strip()
        temp_value = validate_vital_temp(temp_input)
        
        if temp_value == -1:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")
        else:
            break
    
    hr_string = f"HR:{hr_value}"
    temp_string = f"TEMP:{temp_value}"
    
    new_record = f"{ma_er_normalized}|{ten_bn_normalized}|{hr_string}|{temp_string}"
    
    patients.append(new_record)
    
    print("Tiếp nhận ca cấp cứu mới thành công!")


def update_vitals(patients):
    print("\n--- CẬP NHẬT LẠI SINH HIỆU ---")
    
    ma_er = input("Nhập mã ER cần cập nhật: ").strip()
    
    if not ma_er:
        print("Mã ER không được để trống!")
        return
    
    index = find_patient_index(patients, ma_er)
    
    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return
    
    patient = patients[index]
    parts = patient.split('|')
    
    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Sinh hiệu hiện tại: {parts[2]} | {parts[3]}")
    
    print("Bạn muốn cập nhật:")
    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")
    
    try:
        chon = int(input("Chọn loại sinh hiệu: "))
    except ValueError:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")
        return
    
    if chon == 1:
        while True:
            hr_input = input("Nhập nhịp tim mới: ").strip()
            hr_value = validate_vital_hr(hr_input)
            
            if hr_value == -1:
                print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            else:
                break
        
        parts[2] = f"HR:{hr_value}"
        new_record = "|".join(parts)
        patients[index] = new_record
        
        print("Cập nhật nhịp tim thành công!")
    
    elif chon == 2:
        while True:
            temp_input = input("Nhập nhiệt độ mới: ").strip()
            temp_value = validate_vital_temp(temp_input)
            
            if temp_value == -1:
                print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")
            else:
                break
        
        parts[3] = f"TEMP:{temp_value}"
        new_record = "|".join(parts)
        patients[index] = new_record
        
        print("Cập nhật nhiệt độ thành công!")
    
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")


def trigger_red_alert(patients):
    print("\n--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")
    
    if not patients:
        print("Khoa cấp cứu hiện đang trống.")
        return
    
    critical_patients = []
    
    for patient in patients:
        parts = patient.split('|')
        hr_raw = parts[2]
        temp_raw = parts[3]
        
        hr_value = extract_vital_value(hr_raw)
        temp_value = extract_vital_value(temp_raw)
        
        if hr_value > 100 or temp_value >= 39.0:
            critical_patients.append(parts)
    
    if not critical_patients:
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
        return
    
    print("\n!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")
    
    for index, parts in enumerate(critical_patients, 1):
        ma_er = parts[0]
        ten_bn = parts[1]
        hr_raw = parts[2]
        temp_raw = parts[3]
        
        hr_value = extract_vital_value(hr_raw)
        temp_value = extract_vital_value(temp_raw)
        
        print(f"{index}. [{ma_er}] {ten_bn:<20} | HR: {hr_value} bpm | TEMP: {temp_value} °C | CẦN XỬ LÝ KHẨN CẤP")
    
    print("-----------------------------------------------------")
    print(f"Tổng số ca nguy kịch: {len(critical_patients)}")


def discharge_patient(patients):
    print("\n--- XUẤT VIỆN / CHUYỂN KHOA ---")
    
    ma_er = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip()
    
    if not ma_er:
        print("Mã ER không được để trống!")
        return
    
    index = find_patient_index(patients, ma_er)
    
    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return
    
    patient = patients[index]
    parts = patient.split('|')
    ten_bn = parts[1]
    
    patients.pop(index)
    
    print(f"Đã chuyển khoa thành công cho bệnh nhân {ten_bn}!")

def main():
    local_patients = er_patients
    
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
        print("1. Bảng theo dõi bệnh nhân")
        print("2. Tiếp nhận ca cấp cứu mới")
        print("3. Cập nhật lại sinh hiệu")
        print("4. BÁO ĐỘNG ĐỎ Lọc bệnh nhân nguy kịch")
        print("5. Xuất viện / Chuyển khoa")
        print("6. Thoát chương trình")
        print("=================================================")
        
        try:
            chon = int(input("Chọn chức năng (1-6): "))
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-6!")
            continue
        
        if chon == 1:
            display_dashboard(local_patients)
        elif chon == 2:
            admit_patient(local_patients)
        elif chon == 3:
            update_vitals(local_patients)
        elif chon == 4:
            trigger_red_alert(local_patients)
        elif chon == 5:
            discharge_patient(local_patients)
        elif chon == 6:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Kết thúc ca trực!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-6!")


if __name__ == "__main__":
    main()