# Bài 1. In lời chào
name = input("Nhập tên của bạn: ")

print(f"Hello, {name}")


# # Bài 2. Nhập tuổi
# age = int(input("Nhập tuổi: "))

# print(f"You are {age} years old")


# # Bài 3. Cộng hai số nguyên
# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))

# print("Tổng =", a + b)


# # Bài 4. Tính diện tích hình chữ nhật
# length = float(input("Nhập chiều dài: "))
# width = float(input("Nhập chiều rộng: "))

# area = length * width

# print("Diện tích =", area)


# # Bài 5. Kiểm tra kiểu dữ liệu
# name = "John"
# age = 20
# score = 8.5
# is_student = True

# print(type(name))
# print(type(age))
# print(type(score))
# print(type(is_student))


# # Bài 6. Tính chu vi hình tròn
# r = float(input("Nhập bán kính: "))

# c = 2 * 3.14 * r

# print("Chu vi =", c)


# # Bài 7. Chia lấy phần nguyên và phần dư
# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))

# print("Phần nguyên:", a // b)
# print("Phần dư:", a % b)


# # Bài 8. Kiểm tra số chẵn lẻ
# n = int(input("Nhập số nguyên: "))

# if n % 2 == 0:
#     print("Số chẵn")
# else:
#     print("Số lẻ")


# # Bài 9. Kiểm tra tuổi trưởng thành
# age = int(input("Nhập tuổi: "))

# if age >= 16:
#     print("Đủ tuổi làm căn cước công dân")
# else:
#     print("Không đủ tuổi")


# # Bài 10. Tính điểm trung bình
# math = float(input("Điểm Toán: "))
# literature = float(input("Điểm Văn: "))
# english = float(input("Điểm Anh: "))

# average = (math + literature + english) / 3

# print("Điểm trung bình =", average)


# # Bài 11. Xếp loại học lực
# avg = float(input("Nhập điểm trung bình: "))

# if avg >= 8:
#     print("Good")
# elif avg >= 6.5:
#     print("Fair")
# elif avg >= 5:
#     print("Average")
# else:
#     print("Weak")


# # Bài 12. Tìm số lớn nhất trong 3 số
# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))
# c = int(input("Nhập c: "))

# print("Số lớn nhất là:", max(a, b, c))


# # Bài 13. Kiểm tra năm nhuận
# year = int(input("Nhập năm: "))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Là năm nhuận")
# else:
#     print("Không phải năm nhuận")


# # Bài 14. In các số từ 1 đến n
# n = int(input("Nhập n: "))

# for i in range(1, n + 1):
#     print(i)


# # Bài 15. Tính tổng từ 1 đến n
# n = int(input("Nhập n: "))

# total = 0

# for i in range(1, n + 1):
#     total += i

# print("Tổng =", total)


# # Bài 16. In bảng cửu chương
# n = int(input("Nhập số: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")


# # Bài 17. Đếm số chẵn từ 1 đến n
# n = int(input("Nhập n: "))

# count = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         count += 1

# print("Có", count, "số chẵn")


# # Bài 18. Đếm số ký tự trong chuỗi
# text = input("Nhập chuỗi: ")

# print("Độ dài chuỗi =", len(text))


# # Bài 19. Kiểm tra chuỗi đối xứng
# text = input("Nhập chuỗi: ")

# if text == text[::-1]:
#     print("Chuỗi đối xứng")
# else:
#     print("Chuỗi không đối xứng")