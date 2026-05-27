def main():
    n = int(input("Nhập số lượng hóa dơn trong ca: "))

    for i in range(1, n + 1):
        price = int(input(f"Nhập giá trị hóa đơn thứ {i}: "))
        max_price = price if i == 1 else max(max_price, price)
        min_price = price if i == 1 else min(min_price, price)
    print(f"--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
    print(f"Giá trị hóa đơn cao nhất: {max_price:,.0f} VND")
    print(f"Giá trị hóa đơn thấp nhất: {min_price:,.0f} VND")

if __name__ == "__main__":
    main()