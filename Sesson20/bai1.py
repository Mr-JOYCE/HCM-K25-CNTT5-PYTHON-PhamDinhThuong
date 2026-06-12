# 1. Tại sao xuất hiện lỗi ZeroDivisionError: division by zero?
#
# Khi xử lý dữ liệu của ShowMaker:
# ("ShowMaker", "15", "0", "10")
#
# Giá trị Deaths = "0"
# Sau khi ép kiểu:
#
#     (int("15") + int("10")) / int("0")
#     = 25 / 0
#
# Trong Python, phép chia cho 0 không hợp lệ nên phát sinh
# ngoại lệ ZeroDivisionError.
#
# Vì chương trình không sử dụng try-except để xử lý ngoại lệ,
# chương trình sẽ dừng ngay lập tức và không tiếp tục xử lý
# các tuyển thủ còn lại trong danh sách.


# 2. Nếu xóa ShowMaker thì Chovy sẽ gặp lỗi gì?
#
# Dữ liệu của Chovy:
# ("Chovy", "12", "ba", "5")
#
# Khi thực hiện:
#
#     int("ba")
#
# Python không thể chuyển chuỗi "ba" thành số nguyên.
#
# Do đó phát sinh ngoại lệ:
#
#     ValueError:
#     invalid literal for int() with base 10: 'ba'
#
# Đây là lỗi ValueError vì giá trị nhận được không đúng
# định dạng số nguyên mà hàm int() yêu cầu.


# 3. Đánh giá cách đặt tên biến theo chuẩn Clean Code
#
# Code cũ:
#
#     ds, x, n, k, d, a
#
# Các tên biến quá ngắn và không thể hiện ý nghĩa nghiệp vụ.
# Người đọc phải đoán chức năng của từng biến.
#
# Đề xuất đổi tên:
#
#     ds -> player_stats_list
#     x  -> player_stats
#     n  -> player_name
#     k  -> kills
#     d  -> deaths
#     a  -> assists
#
# Những tên biến này giúp code tự mô tả ý nghĩa
# (Self-documenting Code), dễ đọc và dễ bảo trì hơn.


# 4. Lợi ích của việc tách hàm calculate_kda()
#
# Ví dụ:
#
#     def calculate_kda(kills, deaths, assists):
#         return (kills + assists) / deaths
#
# Việc tách riêng công thức tính KDA giúp:
#
# - Tuân thủ nguyên tắc DRY (Don't Repeat Yourself).
# - Tránh lặp lại công thức ở nhiều nơi.
# - Dễ tái sử dụng trong các module khác.
# - Dễ kiểm thử (Unit Test).
# - Dễ bảo trì khi công thức KDA thay đổi.
# - Giúp hàm chính ngắn gọn và dễ đọc hơn.
#
# Đây cũng là cách áp dụng nguyên tắc Single Responsibility,
# mỗi hàm chỉ nên đảm nhận một nhiệm vụ cụ thể.

# Dữ liệu thống kê
player_stats_list = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def calculate_kda(kills, deaths, assists):
    """
    Tính chỉ số KDA.
    """
    return (kills + assists) / deaths


def process_player_stats(player_stats_list):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player_stats in player_stats_list:
        name, kills, deaths, assists = player_stats

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(
                kills,
                deaths,
                assists
            )

            print(
                f"Tuyển thủ {name} có chỉ số KDA là: {kda}"
            )

        except ZeroDivisionError:
            print(
                f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!"
            )
            continue

        except ValueError:
            print(
                f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!"
            )
            continue

    print("--- HOÀN TẤT ---")


process_player_stats(player_stats_list)