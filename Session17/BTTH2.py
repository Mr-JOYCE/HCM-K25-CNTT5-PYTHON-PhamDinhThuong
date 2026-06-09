# --- 1. KHỞI TẠO DỮ LIỆU ---
product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5",
    "P04-Sạc Dự Phòng-300000" 
]

def reduce_custom(function, iterable, initial=None):
    it = iter(iterable)
    if initial is None:
        accumulator = next(it)
    else:
        accumulator = initial
    
    for item in it:
        accumulator = function(accumulator, item)
    
    return accumulator

def parse_price(price_str):
    cleaned = ''.join(filter(lambda x: x.isdigit() or x == '.', price_str))
    try:
        return int(cleaned)
    except ValueError:
        return 0

def get_product_dict(item_str):
    parts = item_str.split('-')
    
    if len(parts) < 4:
        ma = parts[0] if parts else "Unknown"
        print(f"Bỏ qua sản phẩm {ma} do sai cấu trúc dữ liệu.")
        return None

    try:
        ma_sp = parts[0]
        ten_sp = parts[1]
        gia_tien = parse_price(parts[2])
        rating = float(parts[3])
    except (ValueError, IndexError):
        return None

    return {
        'code': ma_sp,
        'name': ten_sp,
        'price': gia_tien,
        'rating': rating
    }

def hien_thi_label():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    for item in product_list:
        info = get_product_dict(item)
        if info is None:
            continue
        
        print(f"Mã: {info['code']:<10} | Tên: {info['name']:<25} | Giá: {info['price']:>12,} VND | Rating: {info['rating']}*")

def sap_xep_san_pham():
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    
    product_list.sort(key=lambda x: (
        -get_product_dict(x)['price'], 
        get_product_dict(x)['price']
    ))
    
    product_list.sort(key=lambda x: (
        -get_product_dict(x)['price'], 
        get_product_dict(x)['price']   
    ))
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    for idx, item in enumerate(product_list, 1):
        print(f"{idx}. {item}")

def tinh_tong_gia_tri():
    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    
    prices = [
        get_product_dict(p)['price'] 
        for p in product_list 
        if get_product_dict(p) is not None
    ]
    
    total = reduce_custom(lambda a, b: a + b, prices, 0)
    
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND.")

def main():
    while True:
        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm")
        print("2. Sắp xếp sản phẩm thông minh")
        print("3. Tính tổng giá trị kho hàng")
        print("4. Đóng hệ thống")
        print("================================================")
        
        try:
            chon = int(input("Chọn chức năng (1-4): "))
        except ValueError:
            print("Vui lòng nhập số!")
            continue
        
        if chon == 1:
            hien_thi_label()
        elif chon == 2:
            sap_xep_san_pham()
        elif chon == 3:
            tinh_tong_gia_tri()
        elif chon == 4:
            print("Cảm ơn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Chức năng không hợp lệ!")

if __name__ == "__main__":
    main()