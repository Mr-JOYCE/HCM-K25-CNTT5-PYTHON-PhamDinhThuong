from datetime import datetime

current_year = datetime.now().year

while True:
    name = input("Nhập tên bệnh nhân: ")

    if len(name.strip()) > 0:
        break
    else:
        print("Vui lòng nhập tên")

while True:
    birth_year = input("Năm sinh: ")

    if birth_year.isdigit():

        birth_year = int(birth_year)

        if 1900 <= birth_year <= current_year:
            break

    print("Năm sinh không hợp lệ")

while True:
    number_sick = input("Số ngày bệnh: ")

    if number_sick.isdigit():

        number_sick = int(number_sick)

        if number_sick >= 0:
            break

    print("Số ngày bệnh không hợp lệ")

while True:
    try:
        heat_body = float(input("Nhiệt độ cơ thể (°C): "))

        if 30 <= heat_body <= 45:
            break
        else:
            print("Nhiệt độ cơ thể không hợp lệ")

    except:
        print("Vui lòng nhập số thực")

while True:
    try:
        price = float(input("Chi phí khám (VNĐ): "))

        if price > 0:
            break
        else:
            print("Số tiền phải > 0")

    except:
        print("Vui lòng nhập số")

age = current_year - birth_year

extra_price = price * 0.10

total_price = price + extra_price

if heat_body > 38 and number_sick > 3:
    status = "Nguy hiểm"

elif heat_body > 38:
    status = "Sốt cao"

elif heat_body > 37.5:
    status = "Sốt nhẹ"

else:
    status = "Bình thường"

if status == "Nguy hiểm":

    if age > 60:
        message = "Cấp cứu"
    else:
        message = "Ưu tiên cao"

else:
    message = "Bình thường"

evaluate = "Cao" if total_price > 500000 else "Thấp"

def printf():

    print("\n--- KẾT QUẢ ---")

    print(f"Tên: {name}")
    print(f"Tuổi: {age}")
    print(f"Nhiệt độ: {heat_body}")
    print(f"Số ngày bệnh: {number_sick}")

    print("\nTình trạng:", status)
    print("Mức độ ưu tiên:", message)

    print(f"\nTổng chi phí: {total_price:,.0f} VNĐ")
    print(f"Mức chi phí: {evaluate}")

printf()