while True:
    while True:
        so_luong = input("Nhập số lượng nhân viên: ")

        if so_luong.isdigit() and int(so_luong) > 0:
            so_luong = int(so_luong)
            break
        else:
            print("Vui lòng nhập số hợp lệ")

    for i in range(1, so_luong + 1):
        print(f"\nNhân viên {i}")

        ten = input("Tên nhân viên: ")

        while True:
            ngay_lam = input("Số ngày đi làm: ")

            if ngay_lam.isdigit() and 0 <= int(ngay_lam) <= 31:
                ngay_lam = int(ngay_lam)
                break
            else:
                print("Số ngày đi làm không hợp lệ")

        print("Thông tin nhân viên:")
        print(f"Tên: {ten}")
        print(f"Số ngày đi làm: {ngay_lam}")

        if ngay_lam < 20:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")

    tiep_tuc = input("\nTiếp tục chương trình? (y/n): ").lower()

    if tiep_tuc == "n":
        print("Chương trình kết thúc")
        break