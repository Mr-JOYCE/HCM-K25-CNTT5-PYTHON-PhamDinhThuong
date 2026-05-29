def main():
    count_revenue = 0
    for i in range(1, 8):
        revenue = int(input(f"Nhập doanh thu ngày {i}: "))
        if i == 1:
            sum_revenue = revenue
        else:
            sum_revenue += revenue
        if revenue >= 5000000:
            if count_revenue in locals():
                count_revenue += 1
            else:
                count_revenue = 1

    average_revenue = sum_revenue / 7

    print(f"--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
    print(f"Tổng doanh thu cả tuần: {sum_revenue:,.0f} VND")
    print(f"Trung bình doanh thu mỗi ngày: {average_revenue:,.0f} VND")
    print(f"Số ngày đạt doanh thu mục tiêu (>= 5.000.000 VND): {count_revenue} ngày")



if __name__ == "__main__":
    main()