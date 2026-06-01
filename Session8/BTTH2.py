def normalize_keywords(raw):
    if raw is None:
        return []
    parts = [k.strip() for k in raw.split(',')]
    return [k for k in parts if k != ""]


def normalize_category(raw):
    if raw is None:
        return ''
    s = ' '.join(raw.strip().split())
    return s.lower()


def normalize_shop_name(raw):
    if raw is None:
        return ''
    s = raw.strip().lower()
    s = '-'.join(s.split())
    if not s.startswith('shop-'):
        s = 'shop-' + s
    return s


def is_valid_promo(code):
    if code is None or code == '':
        return False, 'Mã giảm giá không được rỗng'
    if ' ' in code:
        return False, 'Mã giảm giá không được chứa khoảng trắng'
    if not (6 <= len(code) <= 12):
        return False, 'Mã giảm giá phải có độ dài từ 6 đến 12 ký tự'
    if code.upper() != code:
        return False, 'Mã giảm giá phải được viết hoa toàn bộ'
    if not code.isalnum():
        return False, 'Mã giảm giá chỉ được chứa chữ cái và chữ số'
    if not code.startswith('SALE'):
        return False, "Mã giảm giá phải bắt đầu bằng chuỗi 'SALE'"
    return True, None


def menu():
    print('\n=== Hệ thống quản lý & chuẩn hóa thông tin sản phẩm (Shopee) ===')
    print('1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê')
    print('2. Chuẩn hóa tên Shop')
    print('3. Kiểm tra mã giảm giá hợp lệ')
    print('4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm')
    print('5. Thoát chương trình')


def main():
    shop_name = None
    product_name = None
    description = None
    category = None
    keywords = []
    promo_codes = []

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
            raw_shop = input('Nhập tên Shop: ')
            if raw_shop is None or raw_shop.strip() == '':
                print('Tên shop không được bỏ trống')
                continue
            shop_name = raw_shop.strip()

            raw_product = input('Nhập tên sản phẩm: ')
            product_name = raw_product.strip() if raw_product is not None else ''

            raw_desc = input('Nhập mô tả sản phẩm: ')
            if raw_desc is None or raw_desc.strip() == '':
                print('Mô tả sản phẩm không được rỗng')
                continue
            description = raw_desc.strip()

            raw_category = input('Nhập danh mục sản phẩm: ')
            category = normalize_category(raw_category)

            raw_keywords = input('Nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ')
            keywords = normalize_keywords(raw_keywords)

            print('\n--- Báo cáo thống kê sản phẩm ---')
            print('Tên shop sau khi loại bỏ khoảng trắng đầu và cuối:', shop_name)
            print('Tên sản phẩm (viết hoa chữ cái đầu mỗi từ):', product_name.title())
            print('Mô tả sản phẩm sau khi loại bỏ khoảng trắng đầu và cuối:', description)
            print('Độ dài mô tả sản phẩm (số ký tự):', len(description))
            print('Danh mục sản phẩm sau khi chuẩn hóa (chữ thường):', category)
            print('Danh sách từ khóa sau khi chuẩn hóa khoảng trắng:', keywords)
            print('Số lượng từ khóa tìm kiếm:', len(keywords))
            print('Mô tả toàn chữ thường:', description.lower())
            print('Mô tả toàn chữ hoa:', description.upper())

        elif opt == 2:
            raw = input('Nhập tên shop ban đầu: ')
            if raw is None or raw.strip() == '':
                print('Tên shop không được bỏ trống')
                continue
            original = raw
            normalized = normalize_shop_name(original)
            print('Tên shop ban đầu:', original)
            print('Tên shop sau khi được chuẩn hóa:', normalized)

        elif opt == 3:
            code = input('Nhập mã giảm giá cần kiểm tra: ')
            valid, reason = is_valid_promo(code)
            if valid:
                print('Mã giảm giá hợp lệ')
                if code not in promo_codes:
                    promo_codes.append(code)
                print('Danh sách mã giảm giá hiện tại:', promo_codes)
            else:
                print('Mã giảm giá không hợp lệ:', reason)

        elif opt == 4:
            if description is None or description.strip() == '':
                print('Chưa có mô tả sản phẩm hợp lệ. Vui lòng nhập dữ liệu qua chức năng 1 trước.')
                continue
            find = input('Nhập từ khóa cần tìm: ')
            replace = input('Nhập từ khóa thay thế: ')
            if find == '':
                print('Từ khóa tìm kiếm không được rỗng')
                continue
            count = description.count(find)
            if count == 0:
                print('Không tìm thấy từ khóa cần tìm trong mô tả sản phẩm.')
            else:
                description = description.replace(find, replace)
                print('Số lần xuất hiện của từ khóa:', count)
                print('Mô tả sau khi thay thế:')
                print(description)

        elif opt == 5:
            print('Thoát chương trình')
            break


if __name__ == '__main__':
    main()
