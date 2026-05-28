def input_positive_int(prompt):
	while True:
		try:
			val = int(input(prompt))
			if val < 0:
				print("Giá trị không hợp lệ: không được nhập số âm. Thử lại.")
				continue
			if val == 0:
				print("Giá trị không hợp lệ: không được nhập 0. Thử lại.")
				continue
			return val
		except ValueError:
			print("Vui lòng nhập một số nguyên hợp lệ.")


def choose_item():
	print("Chọn mặt hàng: 1-Laptop, 2-Phone, 3-Tablet")
	while True:
		try:
			choice = int(input("Mã mặt hàng (1-3): "))
			if choice in (1, 2, 3):
				return choice
			print("Lựa chọn không hợp lệ. Vui lòng nhập 1, 2 hoặc 3.")
		except ValueError:
			print("Vui lòng nhập một số nguyên hợp lệ.")


def print_stars(count):
	return '*' * count


def main():
	qty_laptop = 0
	qty_phone = 0
	qty_tablet = 0

	while True:
		print('\n=== HỆ THỐNG QUẢN LÝ KHO - MENU ===')
		print('1. Xem báo cáo tồn kho')
		print('2. Nhập kho')
		print('3. Xuất kho')
		print('4. Cảnh báo hàng tồn kho thấp')
		print('5. Thoát chương trình')

		choice = input('Chọn chức năng (1-5): ').strip()
		if not choice.isdigit():
			print('Lựa chọn không hợp lệ. Vui lòng nhập số 1-5.')
			continue
		choice = int(choice)

		if choice == 1:
			print('\n--- Báo cáo tồn kho hiện tại ---')
			print(f'Laptop ({qty_laptop}): {print_stars(qty_laptop)}')
			print(f'Phone  ({qty_phone}): {print_stars(qty_phone)}')
			print(f'Tablet ({qty_tablet}): {print_stars(qty_tablet)}')

		elif choice == 2:
			item = choose_item()
			qty = input_positive_int('Nhập số lượng thêm: ')
			if item == 1:
				qty_laptop += qty
				print(f'Đã nhập {qty} Laptop. Tồn kho mới: {qty_laptop}')
			elif item == 2:
				qty_phone += qty
				print(f'Đã nhập {qty} Phone. Tồn kho mới: {qty_phone}')
			else:
				qty_tablet += qty
				print(f'Đã nhập {qty} Tablet. Tồn kho mới: {qty_tablet}')

		elif choice == 3:
			item = choose_item()
			qty = input_positive_int('Nhập số lượng xuất: ')
			if item == 1:
				if qty > qty_laptop:
					print('Không đủ hàng')
				else:
					qty_laptop -= qty
					print(f'Đã xuất {qty} Laptop. Tồn kho mới: {qty_laptop}')
			elif item == 2:
				if qty > qty_phone:
					print('Không đủ hàng')
				else:
					qty_phone -= qty
					print(f'Đã xuất {qty} Phone. Tồn kho mới: {qty_phone}')
			else:
				if qty > qty_tablet:
					print('Không đủ hàng')
				else:
					qty_tablet -= qty
					print(f'Đã xuất {qty} Tablet. Tồn kho mới: {qty_tablet}')

		elif choice == 4:
			print('\n--- Cảnh báo hàng tồn kho thấp (<= 3) ---')
			if qty_laptop <= 3:
				print(f'Cảnh báo: Laptop tồn ít (hiện có {qty_laptop})')
			if qty_phone <= 3:
				print(f'Cảnh báo: Phone tồn ít (hiện có {qty_phone})')
			if qty_tablet <= 3:
				print(f'Cảnh báo: Tablet tồn ít (hiện có {qty_tablet})')
			if qty_laptop > 3 and qty_phone > 3 and qty_tablet > 3:
				print('Tất cả mặt hàng đều đủ số lượng.')

		elif choice == 5:
			print('Thoát chương trình. Tạm biệt!')
			break

		else:
			print('Lựa chọn không hợp lệ. Vui lòng chọn 1-5.')


if __name__ == '__main__':
	main()

