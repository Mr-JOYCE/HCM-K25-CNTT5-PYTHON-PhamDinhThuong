# Bài 1. Tính lương nhân viên
full_name = input("Nhập họ tên nhân viên: ")
working_hours = float(input("Nhập số giờ làm việc: "))
salary_per_hour = float(input("Nhập lương mỗi giờ: "))

salary = working_hours * salary_per_hour

print(f"Nhân viên: {full_name}")
print(f"Lương tháng: {salary:,.0f} VNĐ")


# # Bài 2. Xếp loại học lực
# average_score = float(input("Nhập điểm trung bình: "))

# if average_score >= 8:
#     print("Giỏi")
# elif average_score >= 6.5:
#     print("Khá")
# elif average_score >= 5:
#     print("Trung bình")
# else:
#     print("Yếu")


# # Bài 3. Tính tiền mua hàng
# unit_price = float(input("Nhập đơn giá: "))
# quantity = int(input("Nhập số lượng: "))

# total = unit_price * quantity

# if total > 500000:
#     total *= 0.9

# print(f"Số tiền phải thanh toán: {total:,.0f} VNĐ")


# # Bài 4. Tính tổng từ 1 đến n
# n = int(input("Nhập n: "))

# total = 0

# for i in range(1, n + 1):
#     total += i

# print("Tổng =", total)


# # Bài 5. Đếm số chia hết cho 3
# n = int(input("Nhập n: "))

# count = 0

# for i in range(1, n + 1):
#     if i % 3 == 0:
#         count += 1

# print("Có", count, "số chia hết cho 3")


# # Bài 6. Đăng nhập hệ thống
# correct_username = "admin"
# correct_password = "123456"

# attempt = 0

# while attempt < 3:
#     username = input("Username: ")
#     password = input("Password: ")

#     if username == correct_username and password == correct_password:
#         print("Đăng nhập thành công")
#         break

#     print("Sai tài khoản hoặc mật khẩu")
#     attempt += 1

# if attempt == 3:
#     print("Đã vượt quá số lần đăng nhập")


# # Bài 7. Thống kê doanh thu tuần
# total_revenue = 0

# for day in range(1, 8):
#     revenue = float(input(f"Nhập doanh thu ngày {day}: "))
#     total_revenue += revenue

# average_revenue = total_revenue / 7

# print(f"Tổng doanh thu: {total_revenue:,.0f} VNĐ")
# print(f"Trung bình/ngày: {average_revenue:,.0f} VNĐ")


# # Bài 8. Mô phỏng ATM
# balance = 10000000

# withdraw_amount = int(input("Nhập số tiền muốn rút: "))

# if withdraw_amount > balance:
#     print("Số dư không đủ")
# elif withdraw_amount % 50000 != 0:
#     print("Số tiền phải chia hết cho 50.000")
# else:
#     balance -= withdraw_amount

#     print("Rút tiền thành công")
#     print(f"Số dư còn lại: {balance:,.0f} VNĐ")


# # Bài 9. Quản lý quán cà phê mini
# print("1. Cà phê")
# print("2. Trà sữa")
# print("3. Nước cam")

# choice = int(input("Chọn món: "))
# quantity = int(input("Nhập số lượng: "))

# if choice == 1:
#     price = 25000
# elif choice == 2:
#     price = 35000
# elif choice == 3:
#     price = 30000
# else:
#     print("Món không tồn tại")
#     exit()

# bill = price * quantity

# if bill > 100000:
#     bill *= 0.9

# print(f"Tổng tiền: {bill:,.0f} VNĐ")


# # Bài 10. Kiểm tra số chẵn hay lẻ
# number = int(input("Nhập số nguyên: "))

# if number % 2 == 0:
#     print("Số chẵn")
# else:
#     print("Số lẻ")


# # Bài 11. Tìm số lớn nhất trong 3 số
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# print("Số lớn nhất là:", max(a, b, c))


# # Bài 12. Tính giai thừa
# n = int(input("Nhập n: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print(f"{n}! = {factorial}")


# # Bài 13. Trò chơi đoán số
# secret_number = 7

# while True:
#     guess = int(input("Nhập số dự đoán: "))

#     if guess == secret_number:
#         print("Chúc mừng! Bạn đã đoán đúng.")
#         break

#     print("Sai rồi, hãy thử lại.")


# # Bài 14. Tính cước taxi
# km = float(input("Nhập số km: "))

# if km <= 1:
#     fare = 15000

# elif km <= 10:
#     fare = 15000 + (km - 1) * 12000

# else:
#     fare = 15000 + 9 * 12000 + (km - 10) * 10000

# print(f"Tổng tiền phải trả: {fare:,.0f} VNĐ")