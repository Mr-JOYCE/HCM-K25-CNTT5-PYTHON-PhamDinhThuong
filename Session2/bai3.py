import sys

print("--- PHIEU KHAM BENH DIEN TU ---")

name = input("Nhap ho va ten benh nhan: ")
age_input = input("Nhap tuoi benh nhan: ")

if name is None or name.strip() == "":
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    sys.exit()

try:
    age = int(age_input)
except ValueError:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    sys.exit()

if age < 0 or age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    sys.exit()

if age < 6:
    priority = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif age >= 80:
    priority = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    priority = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print(f"Tên bệnh nhân: {name.strip()}")
print(f"Tuổi: {age}")
print(f"Kết quả phân luồng: {priority}")
