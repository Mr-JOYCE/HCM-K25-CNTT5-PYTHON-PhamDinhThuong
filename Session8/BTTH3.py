def get_nonempty_input(prompt, field_name):
    value = input(prompt)
    if value is None or value.strip() == "":
        print(f"{field_name} không được bỏ trống")
        return None
    return value.strip()


def normalize_whitespace(text):
    return " ".join(text.split())


def title_case_name(text):
    return text.title()


def validate_phone(phone):
    if phone is None or phone.strip() == "":
        return False, "Số điện thoại không hợp lệ"
    phone = phone.strip()
    if not phone.isdigit():
        return False, "Số điện thoại không hợp lệ"
    if len(phone) != 10:
        return False, "Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự"
    return True, phone


def mask_phone(phone):
    return phone[:3] + '*' * 5 + phone[-2:]


def normalize_order_code(raw_code):
    if raw_code is None or raw_code.strip() == "":
        return None, "Mã đơn hàng không được bỏ trống"
    code = raw_code.strip().upper()
    code = '-'.join(code.split())
    if not code.startswith('GRAB-'):
        code = 'GRAB-' + code
    return code, None


def count_words(text):
    return len(text.split())


def main_menu():
    print('\n=== Hệ thống quản lý và chuẩn hóa đơn giao hàng GrabExpress ===')
    print('1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê')
    print('2. Chuẩn hóa mã đơn hàng')
    print('3. Ẩn số điện thoại khách hàng')
    print('4. Tìm kiếm và thay thế từ khóa trong ghi chú giao hàng')
    print('5. Thoát chương trình')


def main():
    order_data = {
        'sender_name': None,
        'sender_phone': None,
        'pickup_address': None,
        'receiver_name': None,
        'receiver_phone': None,
        'delivery_address': None,
        'delivery_note': None,
        'order_code': None,
    }

    while True:
        main_menu()
        choice = input('Chọn chức năng (1-5): ')
        try:
            option = int(choice)
        except ValueError:
            print('Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.')
            continue
        if option < 1 or option > 5:
            print('Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.')
            continue

        if option == 1:
            sender_name = get_nonempty_input('Nhập tên người gửi: ', 'Tên người gửi')
            if sender_name is None:
                continue
            sender_phone = get_nonempty_input('Nhập số điện thoại người gửi: ', 'Số điện thoại')
            if sender_phone is None:
                continue
            pickup_address = get_nonempty_input('Nhập địa chỉ lấy hàng: ', 'Địa chỉ lấy hàng')
            if pickup_address is None:
                continue
            receiver_name = get_nonempty_input('Nhập tên người nhận: ', 'Tên người nhận')
            if receiver_name is None:
                continue
            receiver_phone = get_nonempty_input('Nhập số điện thoại người nhận: ', 'Số điện thoại')
            if receiver_phone is None:
                continue
            delivery_address = get_nonempty_input('Nhập địa chỉ giao hàng: ', 'Địa chỉ giao hàng')
            if delivery_address is None:
                continue
            delivery_note = get_nonempty_input('Nhập ghi chú giao hàng: ', 'Ghi chú giao hàng')
            if delivery_note is None:
                continue

            order_data['sender_name'] = title_case_name(sender_name)
            order_data['sender_phone'] = sender_phone.strip()
            order_data['pickup_address'] = normalize_whitespace(pickup_address)
            order_data['receiver_name'] = title_case_name(receiver_name)
            order_data['receiver_phone'] = receiver_phone.strip()
            order_data['delivery_address'] = normalize_whitespace(delivery_address)
            order_data['delivery_note'] = delivery_note.strip()

            note = order_data['delivery_note']
            print('\n--- Báo cáo thống kê đơn hàng ---')
            print('Tên người gửi:', order_data['sender_name'])
            print('Tên người nhận:', order_data['receiver_name'])
            print('Địa chỉ lấy hàng:', order_data['pickup_address'])
            print('Địa chỉ giao hàng:', order_data['delivery_address'])
            print('Ghi chú giao hàng:', note)
            print('Độ dài ghi chú giao hàng:', len(note))
            print('Số lượng từ trong ghi chú giao hàng:', count_words(note))
            print('Ghi chú giao hàng chữ thường:', note.lower())
            print('Ghi chú giao hàng chữ hoa:', note.upper())

        elif option == 2:
            raw_code = input('Nhập mã đơn hàng: ')
            normalized_code, error = normalize_order_code(raw_code)
            if error:
                print(error)
                continue
            order_data['order_code'] = normalized_code
            print('Mã đơn hàng ban đầu:', raw_code)
            print('Mã đơn hàng sau khi được chuẩn hóa:', normalized_code)

        elif option == 3:
            sender_phone = order_data['sender_phone']
            receiver_phone = order_data['receiver_phone']
            if sender_phone is None:
                sender_phone = get_nonempty_input('Nhập số điện thoại người gửi: ', 'Số điện thoại')
                if sender_phone is None:
                    continue
            if receiver_phone is None:
                receiver_phone = get_nonempty_input('Nhập số điện thoại người nhận: ', 'Số điện thoại')
                if receiver_phone is None:
                    continue

            valid_sender, sender_value = validate_phone(sender_phone)
            if not valid_sender:
                print(sender_value)
                continue
            valid_receiver, receiver_value = validate_phone(receiver_phone)
            if not valid_receiver:
                print(receiver_value)
                continue

            order_data['sender_phone'] = sender_value
            order_data['receiver_phone'] = receiver_value
            print('SĐT người gửi:', mask_phone(sender_value))
            print('SĐT người nhận:', mask_phone(receiver_value))

        elif option == 4:
            note = order_data['delivery_note']
            if note is None or note.strip() == "":
                print('Chưa có ghi chú giao hàng để tìm kiếm')
                continue

            find_keyword = input('Nhập từ khóa cần tìm: ')
            if find_keyword is None or find_keyword == "":
                print('Từ khóa tìm kiếm không được bỏ trống')
                continue
            replace_keyword = input('Nhập từ khóa thay thế: ')
            if replace_keyword is None:
                replace_keyword = ''

            count = note.count(find_keyword)
            if count == 0:
                print('Không tìm thấy từ khóa cần tìm trong ghi chú giao hàng')
            else:
                note = note.replace(find_keyword, replace_keyword)
                order_data['delivery_note'] = note
                print('Số lần xuất hiện của từ khóa:', count)
                print('Ghi chú đơn hàng sau khi thay thế:')
                print(note)

        elif option == 5:
            print('Thoát chương trình')
            break


if __name__ == '__main__':
    main()
