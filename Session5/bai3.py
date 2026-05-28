print("===== HỆ THỐNG IN SƠ ĐỒ PHÒNG HỌC =====")

room_count = int(input("Nhập số lượng phòng học: "))

if room_count <= 0:

    print("Số lượng phòng học không hợp lệ")
    print("Chương trình kết thúc")

else:
    for room_number in range(1, room_count + 1):

        print(f"\n===== PHÒNG HỌC {room_number} =====")

        row_count = int(input("Nhập số hàng ghế: "))

        seat_count = int(input("Nhập số ghế trên mỗi hàng: "))

        if row_count <= 0 or seat_count <= 0:

            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if row_count > 10 or seat_count > 10:

            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        print("\nSƠ ĐỒ CHỖ NGỒI:")

        for row in range(row_count):

            print("*" * seat_count)

    print("\nĐã hoàn tất kiểm tra phòng học.")