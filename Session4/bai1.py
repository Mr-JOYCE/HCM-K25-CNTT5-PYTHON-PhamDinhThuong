def main():
    price = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

    if price > 5000000:
        discount = price * 0.1
        final_price = price - discount
    else:
        final_price = price
    
    print(f"--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
    print(f"Số tiền được giảm: {discount if price > 5000000 else 0:,.0f} VND")
    print(f"Tổng số tiền khách phải trả: {final_price:,.0f} VND")


if __name__ == "__main__":
    main()