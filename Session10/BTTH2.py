"""
BTTH2 - He Thong Quan Ly Danh Sach Phat Nhac (CLI)

1) PHAN TICH INPUT / OUTPUT
Input:
- playlist: list[str] luu danh sach ten bai hat theo thu tu.
- Nguoi dung nhap tu ban phim:
  + Lua chon menu chinh (1-5).
  + Lua chon menu phu (them/xoa/sap xep-trich xuat).
  + Ten bai hat (str).
  + Vi tri index khi chen/xoa theo so thu tu (int).

Output:
- Hien thi menu va ket qua thao tac.
- Hien thi danh sach phat voi so thu tu.
- Thong bao loi khi input khong hop le.
- Thong bao so luong bai hat hien tai sau khi them.

2) DE XUAT GIAI PHAP
- Dung list va cac phuong thuc:
  + append(): them cuoi danh sach.
  + insert(index, value): chen vao vi tri cu the.
  + remove(value): xoa theo ten bai hat.
  + pop(index): xoa theo so thu tu.
  + sort(): sap xep A-Z.
  + len(): lay so luong bai hat.
- Dung while True cho menu chinh va menu phu.
- Dung ham kiem tra input so nguyen de tranh crash khi nhap sai.
- Tach ham chuc nang de code ro rang, de bao tri.

3) PSEUDOCODE
BEGIN
  khoi tao playlist (co the rong)
  LOOP menu chinh:
    hien thi menu, nhap choice
    neu choice = 1: menu them bai hat
    neu choice = 2: xem danh sach (neu rong => thong bao)
    neu choice = 3: menu xoa bai hat (neu rong => thong bao)
    neu choice = 4: menu sap xep/trich xuat (neu rong => thong bao)
    neu choice = 5: thoat
    nguoc lai: thong bao choice khong hop le
END
"""


def display_main_menu() -> None:
    """Hien thi menu chinh cua chuong trinh."""
    print("\n========== MENU QUAN LY DANH SACH PHAT ==========")
    print("1. Them bai hat vao danh sach phat")
    print("2. Xem danh sach phat")
    print("3. Xoa bai hat khoi danh sach")
    print("4. Sap xep va trich xuat danh sach")
    print("5. Thoat chuong trinh")
    print("=================================================")


def safe_input_int(prompt: str) -> int | None:
    """
    Doc input so nguyen an toan.
    Tra ve None neu du lieu khong phai so nguyen.
    """
    raw_value = input(prompt).strip()
    try:
        return int(raw_value)
    except ValueError:
        print("Lua chon khong hop le, vui long nhap so nguyen.")
        return None


def ensure_non_empty_playlist(playlist: list[str]) -> bool:
    """Kiem tra danh sach phat co rong hay khong."""
    if not playlist:
        print("Danh sach phat hien dang trong!")
        return False
    return True


def display_playlist(playlist: list[str]) -> None:
    """Hien thi toan bo bai hat trong danh sach phat."""
    if not ensure_non_empty_playlist(playlist):
        return

    print("\n--- DANH SACH PHAT ---")
    for index, song_name in enumerate(playlist, start=1):
        print(f"{index}. {song_name}")
    print(f"\nTong so bai hat: {len(playlist)}")


def add_song_menu(playlist: list[str]) -> None:
    """Menu them bai hat: them cuoi hoac chen vao vi tri cu the."""
    print("\n--- THEM BAI HAT ---")
    print("1. Them vao cuoi danh sach")
    print("2. Chen vao vi tri cu the")

    add_choice = safe_input_int("Nhap lua chon: ")
    if add_choice is None:
        return

    if add_choice not in (1, 2):
        print("Lua chon khong hop le, vui long nhap so nguyen.")
        return

    song_name = input("Nhap ten bai hat: ").strip()
    if not song_name:
        print("Ten bai hat khong duoc de trong.")
        return

    if add_choice == 1:
        playlist.append(song_name)
        print(f'Da them bai hat "{song_name}" vao cuoi danh sach.')
        print(f"So luong bai hat hien tai: {len(playlist)}")
        return

    # add_choice == 2: chen theo so thu tu (1-based)
    position = safe_input_int("Nhap so thu tu muon chen (bat dau tu 1): ")
    if position is None:
        return

    # Cho phep chen tu 1 den len(playlist) + 1
    if position < 1 or position > len(playlist) + 1:
        print("Vi tri khong hop le.")
        return

    playlist.insert(position - 1, song_name)
    print(f'Da chen bai hat "{song_name}" vao vi tri thu {position}.')
    print(f"So luong bai hat hien tai: {len(playlist)}")


def remove_song_menu(playlist: list[str]) -> None:
    """Menu xoa bai hat theo ten hoac theo so thu tu."""
    if not ensure_non_empty_playlist(playlist):
        return

    print("\n--- XOA BAI HAT ---")
    print("1. Xoa theo ten bai hat")
    print("2. Xoa theo so thu tu")

    remove_choice = safe_input_int("Nhap lua chon: ")
    if remove_choice is None:
        return

    if remove_choice == 1:
        song_name = input("Nhap ten bai hat can xoa: ").strip()
        if song_name in playlist:
            playlist.remove(song_name)
            print(f'Da xoa bai hat "{song_name}" khoi danh sach.')
        else:
            print("Khong tim thay bai hat trong danh sach phat.")
    elif remove_choice == 2:
        position = safe_input_int("Nhap so thu tu bai hat can xoa: ")
        if position is None:
            return

        if position < 1 or position > len(playlist):
            print("Vi tri khong hop le.")
            return

        removed_song = playlist.pop(position - 1)
        print(f'Da xoa bai hat "{removed_song}" khoi danh sach.')
    else:
        print("Lua chon khong hop le, vui long nhap so nguyen.")


def sort_extract_menu(playlist: list[str]) -> None:
    """Menu sap xep danh sach va trich xuat 3 bai hat dau tien."""
    if not ensure_non_empty_playlist(playlist):
        return

    print("\n--- SAP XEP VA TRICH XUAT DANH SACH ---")
    print("1. Sap xep danh sach phat theo bang chu cai A-Z")
    print("2. Hien thi 3 bai hat dau tien")

    action_choice = safe_input_int("Nhap lua chon: ")
    if action_choice is None:
        return

    if action_choice == 1:
        playlist.sort()
        print("Da sap xep danh sach phat theo thu tu A-Z.")
        display_playlist(playlist)
    elif action_choice == 2:
        print("\n--- DANH SACH PHAT ---")
        first_three = playlist[:3]
        for index, song_name in enumerate(first_three, start=1):
            print(f"{index}. {song_name}")
        print(f"\nTong so bai hat: {len(first_three)}")
    else:
        print("Lua chon khong hop le, vui long nhap so nguyen.")


def main() -> None:
    """Ham dieu khien chuong trinh chinh."""
    playlist: list[str] = []

    while True:
        display_main_menu()
        choice = safe_input_int("Nhap lua chon cua ban: ")

        if choice is None:
            continue

        if choice == 1:
            add_song_menu(playlist)
        elif choice == 2:
            display_playlist(playlist)
        elif choice == 3:
            remove_song_menu(playlist)
        elif choice == 4:
            sort_extract_menu(playlist)
        elif choice == 5:
            print("Cam on ban da su dung dich vu. Tam biet!")
            break
        else:
            print("Lua chon khong hop le, vui long nhap so nguyen.")


if __name__ == "__main__":
    main()
