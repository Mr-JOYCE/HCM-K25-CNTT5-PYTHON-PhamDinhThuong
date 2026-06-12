# 1. Tại sao xuất hiện lỗi IndexError: tuple index out of range?
#
# Dữ liệu của Levi:
# ("Levi", 120, 2500)
#
# Tuple này có 3 phần tử:
# p[0] -> "Levi"
# p[1] -> 120
# p[2] -> 2500
#
# Vì vậy dòng:
#     r = p[2]
# hoạt động bình thường.
#
# Tuy nhiên dữ liệu của SofM:
# ("SofM", 150)
#
# Tuple này chỉ có 2 phần tử:
# p[0] -> "SofM"
# p[1] -> 150
#
# Khi chương trình cố truy cập:
#     p[2]
#
# Python không tìm thấy phần tử ở vị trí thứ 3 nên phát sinh lỗi:
#     IndexError: tuple index out of range
#
# Đây là lỗi xảy ra khi truy cập vào một chỉ số nằm ngoài phạm vi
# của List hoặc Tuple.


# 2. Nếu sửa SofM thành ("SofM", 150, 2800) thì Optimus sẽ gặp lỗi gì?
#
# Dữ liệu của Optimus:
# ("Optimus", 100, "N/A")
#
# Chương trình sẽ chạy tới dòng:
#     b = (m * 10) + (int(r) * 0.5)
#
# Lúc này:
#     r = "N/A"
#
# Python thực hiện:
#     int("N/A")
#
# Hàm int() chỉ chuyển đổi được chuỗi chứa số.
# "N/A" là chuỗi văn bản nên không thể ép kiểu sang số nguyên.
#
# Do đó phát sinh lỗi:
#     ValueError:
#     invalid literal for int() with base 10: 'N/A'
#
# Tên Exception:
#     ValueError


# 3. Lệnh print("Đang xử lý:", p) giúp ích gì trong Debug?
#
# Ví dụ:
#
# for p in ds:
#     print("Đang xử lý:", p)
#
# Khi chạy chương trình:
#
# Đang xử lý: ('Levi', 120, 2500)
# Tuyển thủ Levi nhận được 2450.0 RP
#
# Đang xử lý: ('SofM', 150)
# Traceback...
#
# Nhìn vào kết quả ta biết ngay chương trình bị lỗi khi xử lý
# dữ liệu của SofM.
#
# Đây là một kỹ thuật Debug đơn giản giúp:
# - Xác định bản ghi gây lỗi.
# - Khoanh vùng nguyên nhân lỗi nhanh hơn.
# - Không phải đoán lỗi xảy ra ở vòng lặp nào.
# - Dễ kiểm tra dữ liệu đầu vào từ API.


# 4. Đánh giá cách đặt tên biến theo Clean Code
#
# Các biến hiện tại:
#     ds, p, t, m, r, b
#
# Những tên biến này quá ngắn và không thể hiện ý nghĩa nghiệp vụ.
# Người đọc phải đoán chức năng của từng biến.
#
# Nên đổi thành:
#
# ds -> player_records
# p  -> record
# t  -> name
# m  -> matches
# r  -> mmr
# b  -> bonus
#
# Ví dụ:
#
# for record in player_records:
#     name = record[0]
#     matches = record[1]
#     mmr = record[2]
#
# Cách đặt tên này giúp code tự mô tả ý nghĩa
# (Self-documenting Code), dễ đọc, dễ bảo trì và dễ review hơn.

player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def calculate_bonus(matches, mmr):
    """
    Tính tiền thưởng RP cuối mùa.
    """
    return (matches * 10) + (mmr * 0.5)


def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:

        name = record[0]

        try:
            matches = record[1]
            mmr = int(record[2])

            bonus = calculate_bonus(matches, mmr)

            print(
                f"Tuyển thủ {name} nhận được {bonus} RP"
            )

        except IndexError:
            print(
                f"{name}: Lỗi - Hồ sơ bị thiếu thông tin!"
            )
            continue

        except ValueError:
            print(
                f"{name}: Lỗi - Dữ liệu MMR không hợp lệ!"
            )
            continue

    print("--- HOÀN TẤT ---")


process_bonus(player_records)