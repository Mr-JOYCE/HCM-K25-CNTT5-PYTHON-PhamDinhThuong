def main():
    while True:
        bill = 1
        total_price = 0
        count = 0
        
        price = int(input(f"Khách hàng  {bill} - Nhập giá trị hóa đơn: "))

        if price >= 1000000:
            count += 1


        total_price += price

        comfirm = input("Bạn có muốn nhập hóa đơn tiếp theo không? (C/K): ")
        if comfirm.upper() == "K":
            break
        bill += 1

    ratio_bill = count / bill * 100
    
    print(f"--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
    print(f"Tổng số đơn đã xử lí: {bill} hóa đơn")
    print(f"Tổng doanh thu ngày hôm nay: {total_price:,.0f} VND")
    print(f"Số hóa đơn lớn (>= 1.000.000 VND): {count} hóa đơn")
    print(f"Tỷ lệ hóa đơn lớn so với tổng số hóa đơn: {ratio_bill:.2f}%")

if __name__ == "__main__":
    start = input("Bạn có muốn bắt đầu nhập hóa đơn không? (C/K): ")
    if start.upper() == "C":
        main()