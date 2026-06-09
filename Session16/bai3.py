patients = [
	["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
	["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def  display_patients(patient_list: list):
    if not patient_list: 
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    print(" DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ ".center(52, "-"))
    for i, (id, name, mable, sick) in enumerate(patient_list, start=1):
        print(f"{i}. Mã: {id:<6} | Tên: {name:<15} | Giới tính: {mable:<7} | Bệnh: {sick}")

def validate_gender(gender_input):
    if gender_input == 'nam' or gender_input == 'nu':
        return True
    else:
        return False

def check_patient_code(code):
    for pati in patients:
        if code == pati[0]:
            return False
    else:
        return True



def add_patient(patient_list: list):
    print(" TIẾP NHẬN BỆNH NHÂN MỚI ".center(42, "-"))
    while True:
        id = input("Nhập mã bệnh nhân: ").strip().upper()
        if id.strip() == "":
            print("Dữ liệu không được để trống!")
            continue
        if check_patient_code(id) is False:
            print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
            continue

        

add_patient(patients)