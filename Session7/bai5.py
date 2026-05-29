"""Hệ thống giải mã dữ liệu kho hàng cho Rikkei Store.

Input:
- raw_batch: chuỗi nguyên bản chứa các mã sản phẩm cách nhau bởi ";"
- Người dùng chọn menu 1-4 và nhập đuôi serial khi cần tra cứu.

Output:
- Hiển thị chuỗi mã vạch gốc.
- In báo cáo kiểm kê đã chuẩn hóa theo bảng.
- In thông tin sản phẩm phù hợp khi tra cứu theo 2 ký tự cuối serial.

Giải pháp:
- parse_batch: tách raw_batch theo ";", xóa khoảng trắng, chuyển mã thành chữ hoa.
- decode_item: chia mã sản phẩm theo "-" thành 4 phần, chuẩn hóa năm sản xuất và kiểm tra serial.
- report: in bảng và tính tổng số sản phẩm hợp lệ (Pass) / tổng sản phẩm.
- search: nhận input, strip khoảng trắng, so sánh với 2 ký tự cuối serial.
"""

raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "


def standardize_year(year_part):
    """Chuyển năm sản xuất dạng 2 chữ số sang định dạng 4 chữ số."""
    year_part = year_part.strip()
    if len(year_part) == 2 and year_part.isdigit():
        return f"20{year_part}"
    return year_part


def decode_item(raw_item):
    """Giải mã một mã sản phẩm và xác định trạng thái serial."""
    item = raw_item.strip().upper()
    parts = item.split('-')

    if len(parts) != 4:
        return {
            'product_code': item,
            'product_type': parts[0] if parts else '',
            'origin': parts[1] if len(parts) > 1 else '',
            'year': parts[2] if len(parts) > 2 else '',
            'serial': parts[3] if len(parts) > 3 else '',
            'status': 'Invalid Format',
        }

    product_type = parts[0]
    origin = parts[1]
    year = standardize_year(parts[2])
    serial = parts[3]
    status = 'Pass' if serial.isdigit() else 'Lỗi Serial - Reject'

    return {
        'product_code': item,
        'product_type': product_type,
        'origin': origin,
        'year': year,
        'serial': serial,
        'status': status,
    }


def parse_batch(raw_batch_string):
    """Tách chuỗi raw_batch và trả về danh sách sản phẩm đã giải mã."""
    decoded_items = []
    raw_items = raw_batch_string.split(';')

    for raw_item in raw_items:
        raw_item = raw_item.strip()
        if not raw_item:
            continue
        decoded_items.append(decode_item(raw_item))

    return decoded_items


def print_raw_batch():
    """In chuỗi mã vạch gốc."""
    print('\nChuỗi mã vạch gốc:')
    print(raw_batch)
    print()


def print_inventory_report(items):
    """In báo cáo kiểm kê dưới dạng bảng và tóm tắt số sản phẩm hợp lệ."""
    valid_count = sum(1 for item in items if item['status'] == 'Pass')
    total_count = len(items)

    print('\nBÁO CÁO KIỂM KÊ KHO HÀNG')
    print('-' * 70)
    print(f"{'MÃ SP':<15}{'XUẤT XỨ':<10}{'NĂM SX':<10}{'SERIAL':<10}{'TRẠNG THÁI':<25}")
    print('-' * 70)

    for item in items:
        print(f"{item['product_type']:<15}{item['origin']:<10}{item['year']:<10}{item['serial']:<10}{item['status']:<25}")

    print('-' * 70)
    print(f"Đã giải mã thành công {valid_count} sản phẩm hợp lệ / Tổng số {total_count} sản phẩm.")
    print()


def search_by_serial_suffix(items):
    """Tra cứu sản phẩm theo 2 ký tự cuối của serial."""
    suffix_input = input('Nhập 2 số cuối của Serial cần tìm: ')
    suffix = suffix_input.strip()

    matched_items = []
    for item in items:
        serial = item.get('serial', '')
        if len(serial) >= len(suffix) and serial.endswith(suffix):
            matched_items.append(item)

    if not matched_items:
        print('\nKhông tìm thấy sản phẩm phù hợp')
        print()
        return

    print('\nKết quả tra cứu:')
    for item in matched_items:
        print(f"MÃ SP: {item['product_code']}")
        print(f"Loại SP: {item['product_type']}")
        print(f"Xuất xứ: {item['origin']}")
        print(f"Năm SX: {item['year']}")
        print(f"Serial: {item['serial']}")
        print(f"Trạng thái: {item['status']}\n")


def display_menu():
    """Hiển thị menu chính."""
    print('===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====')
    print('1. Hiển thị chuỗi mã vạch gốc')
    print('2. Giải mã, làm sạch và in báo cáo kiểm kê')
    print('3. Tra cứu nhanh theo đuôi Serial')
    print('4. Thoát chương trình')


def main():
    decoded_items = parse_batch(raw_batch)

    while True:
        display_menu()
        choice = input('Nhập lựa chọn của bạn (1-4): ')

        if not choice.isdigit() or int(choice) not in range(1, 5):
            print('\nChức năng không tồn tại, vui lòng nhập số từ 1-4!\n')
            continue

        option = int(choice)

        if option == 1:
            print_raw_batch()
        elif option == 2:
            print_inventory_report(decoded_items)
        elif option == 3:
            search_by_serial_suffix(decoded_items)
        else:
            print('\nĐóng ca kiểm kho. Chào tạo biệt!')
            break


if __name__ == '__main__':
    main()
