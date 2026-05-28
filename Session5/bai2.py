# LỖI LOGIC:
# Biến total_students được khai báo ngoài vòng lặp chi nhánh,
# nên nó chỉ được khởi tạo đúng 1 lần duy nhất.

# Hệ quả:
# Sau khi tính xong Chi nhánh 1 (83 học viên),
# biến total_students vẫn giữ giá trị 83.

# Khi sang Chi nhánh 2:
# Chương trình tiếp tục cộng thêm số học viên mới
# vào 83 thay vì reset về 0.

# Vì vậy:
# Chi nhánh 2 đúng ra là 60 học viên,
# nhưng hệ thống lại tính:
# 83 + 60 = 143 học viên.

# Tương tự với Chi nhánh 3:
# Hệ thống tiếp tục cộng dồn:
# 143 + 97 = 240 học viên.

# Bản chất lỗi:
# Biến cộng dồn được đặt sai phạm vi (scope).
# Chương trình đang cộng dồn toàn hệ thống,
# nhưng lại dùng kết quả đó để in cho từng chi nhánh.

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

branch_totals = []  # lưu tổng học viên của từng chi nhánh

for branch in range(1, branch_count + 1):
    print(f"\nNhập dữ liệu cho chi nhánh {branch}")
    branch_students = 0  # reset số học viên cho mỗi chi nhánh

    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        branch_students += student_count

    branch_totals.append(branch_students)
    
for branch, total in enumerate(branch_totals, start=1):
    print(f"Chi nhánh {branch}: {total} học viên")
