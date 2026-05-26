import sys

print("--- HE THONG SANG LOC TIEN PHAU THUAT ---")

age_input = input("Nhap tuoi: ")
systolic_input = input("Nhap huyet ap tam thu: ")
blood_sugar_input = input("Nhap duong huyet: ")

try:
    age = int(age_input)
    systolic = int(systolic_input)
    blood_sugar = int(blood_sugar_input)
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ")
    sys.exit()

if age < 0 or systolic < 0 or blood_sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")
    sys.exit()

reasons = []

if age >= 75:
    reasons.append("Tuổi phải dưới 75")
if not (90 <= systolic <= 140):
    reasons.append("Huyết áp tâm thu phải nằm trong khoảng 90-140 mmHg")
if blood_sugar >= 150:
    reasons.append("Đường huyết phải dưới 150 mg/dL")

if reasons:
    print("TỪ CHỐI PHẪU THUẬT")
    for reason in reasons:
        print(f"- {reason}")
else:
    print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
