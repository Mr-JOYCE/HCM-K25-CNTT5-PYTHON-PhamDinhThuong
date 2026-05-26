import sys


BASE_FEE = 500000

def get_valid_insurance_answer():
    while True:
        answer = input("Bạn có thẻ Bảo hiểm Y tế không? (Vui lòng chỉ gõ 'yes' hoặc 'no'): ").strip().lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        print("LỖI: Vui lòng chỉ nhập 'yes' hoặc 'no'.")


print("=== KIOSK PHÂN LUỒNG THÔNG MINH ===")

patient_name = input("Nhập họ và tên bệnh nhân (ví dụ: Nguyen Van A): ").strip()
patient_age_input = input("Nhập tuổi bệnh nhân (ví dụ: 35): ").strip()
spo2_input = input("Nhập nồng độ oxy trong máu SpO2 (ví dụ: 96): ").strip()
heart_rate_input = input("Nhập nhịp tim (ví dụ: 88): ").strip()

try:
    patient_age = int(patient_age_input)
    spo2_level = int(spo2_input)
    heart_rate = int(heart_rate_input)
except ValueError:
    print("LỖI: Vui lòng nhập tuổi, SpO2 và nhịp tim dưới dạng số nguyên.")
    sys.exit()

has_insurance = get_valid_insurance_answer()

if patient_name == "":
    print("LỖI: Họ và tên không được để trống.")
    sys.exit()

if patient_age < 0 or spo2_level < 0 or heart_rate < 0:
    print("LỖI: Dữ liệu nhập vào không hợp lệ.")
    sys.exit()

if spo2_level < 90 or heart_rate > 120:
    triage_result = "BÁO ĐỘNG ĐỎ (Cấp cứu khẩn)"
elif 90 <= spo2_level <= 95 or 100 <= heart_rate <= 120:
    triage_result = "BÁO ĐỘNG VÀNG (Theo dõi sát)"
else:
    triage_result = "XANH (Khám thường)"

if patient_age < 6 or patient_age >= 80:
    estimated_fee = 0
elif has_insurance:
    estimated_fee = 250000
else:
    estimated_fee = BASE_FEE

print("\n=== PHIẾU KHÁM BỆNH ĐIỆN TỬ ===")
print(f"Tên bệnh nhân: {patient_name}")
print(f"Tuổi: {patient_age}")
print(f"SpO2: {spo2_level}%")
print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f"Có BHYT: {'Có' if has_insurance else 'Không'}")
print(f"Phân luồng: {triage_result}")
print(f"Tạm ứng viện phí: {estimated_fee:,.0f} VNĐ")