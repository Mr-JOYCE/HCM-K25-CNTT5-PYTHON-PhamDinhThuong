def input_nonempty(prompt, error_msg):
    while True:
        val = input(prompt)
        if val.strip() == "":
            print(error_msg)
            return None
        return val


def normalize_hashtags(raw):
    if raw is None:
        return []
    parts = [h.strip() for h in raw.split(',')]
    return [h for h in parts if h != ""]


def is_valid_hashtag(tag):
    if tag is None or tag == "":
        return False, "Hashtag không được rỗng"
    if not tag.startswith('#'):
        return False, "Hashtag phải bắt đầu bằng ký tự '#'"
    if ' ' in tag:
        return False, "Hashtag không được chứa khoảng trắng"
    if len(tag) < 2:
        return False, "Hashtag phải có ít nhất 2 ký tự (bao gồm '#')"
    body = tag[1:]
    if not all(c.isalnum() or c == '_' for c in body):
        return False, "Hashtag chỉ được chứa chữ, số hoặc dấu gạch dưới sau '#'"
    return True, None


def menu():
    width = 52
    print("+" + "=" * (width - 2) + "+")
    print("|" + " " * ((width - 33) // 2) + "HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK" + " " * ((width - 33) // 2) + "|")
    print("+" + "=" * (width - 2) + "+")
    print(f"| {'1. Nhập và phân tích thông tin video':<48} |")
    print(f"| {'2. Chuẩn hóa tên tài khoản':<48} |")
    print(f"| {'3. Kiểm tra tính hợp lệ của hagtag':<48} |")
    print(f"| {'4. Tìm kiếm và thay thế từ khóa trong mô tả':<48} |")
    print(f"| {'5. Thoát chương trình':<48} |")
    print("+" + "=" * (width - 1))


def main():
    username = None
    title = None
    description = None
    hashtags = []

    while True:
        menu()
        choice = input('Chọn chức năng (1-5): ')
        try:
            opt = int(choice)
        except ValueError:
            print('Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.')
            continue
        if opt < 1 or opt > 5:
            print('Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.')
            continue

        if opt == 1:
            raw_user = input('Nhập tên tài khoản người đăng video: ')
            if raw_user is None or raw_user.strip() == "":
                print('Tên tài khoản không được rỗng')
                continue
            username = raw_user.strip()

            raw_title = input('Nhập tiêu đề video: ')
            title = raw_title.strip() if raw_title is not None else ''

            raw_desc = input('Nhập mô tả video: ')
            if raw_desc is None or raw_desc.strip() == "":
                print('Mô tả video không được rỗng')
                continue
            description = raw_desc.strip()

            raw_tags = input('Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ')
            hashtags = normalize_hashtags(raw_tags)

            print('\n--- Báo cáo thống kê video ---')
            print('Tên tài khoản sau khi loại bỏ khoảng trắng đầu và cuối:', username)
            print('Tiêu đề (viết hoa chữ cái đầu mỗi từ):', title.title())
            print('Mô tả sau khi loại bỏ khoảng trắng đầu và cuối:', description)
            print('Độ dài mô tả (số ký tự):', len(description))

            word_count = len(description.split()) if description else 0
            print('Số lượng từ trong mô tả video:', word_count)
            print('Danh sách hashtag sau khi chuẩn hóa khoảng trắng:', hashtags)
            print('Số lượng hashtag:', len(hashtags))
            print('Mô tả toàn chữ thường:', description.lower())
            print('Mô tả toàn chữ hoa:', description.upper())

        elif opt == 2:
            raw = input('Nhập tên tài khoản ban đầu: ')
            if raw is None or raw.strip() == "":
                print('Tên tài khoản không được rỗng')
                continue
            original = raw
            n = original.strip().lower()
            if not n.startswith('@'):
                n = '@' + n
            print('Tên tài khoản ban đầu:', original)
            print('Tên tài khoản sau khi được chuẩn hoá:', n)

        elif opt == 3:
            tag = input('Nhập hashtag cần kiểm tra: ')
            valid, reason = is_valid_hashtag(tag)
            if valid:
                print('Hashtag hợp lệ')
                if tag not in hashtags:
                    hashtags.append(tag)
                    print('Đã thêm hashtag vào danh sách hiện tại.')
                else:
                    print('Hashtag đã tồn tại trong danh sách.')
            else:
                print('Hashtag không hợp lệ:', reason)

        elif opt == 4:
            if description is None or description.strip() == "":
                print('Chưa có mô tả video hợp lệ. Vui lòng nhập dữ liệu qua chức năng 1 trước.')
                continue
            find = input('Nhập từ khóa cần tìm: ')
            replace = input('Nhập từ khóa thay thế: ')
            if find == "":
                print('Từ khóa tìm kiếm không được rỗng')
                continue
            count = description.count(find)
            if count == 0:
                print('Không tìm thấy từ khóa cần tìm trong mô tả.')
            else:
                description = description.replace(find, replace)
                print('Mô tả sau khi thay thế:')
                print(description)
                print('Số lần từ khóa xuất hiện trước khi thay thế:', count)

        elif opt == 5:
            print('Thoát chương trình')
            break


if __name__ == '__main__':
    main()
