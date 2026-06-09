raw_logs: list[str] = []
processed_logs: list[str] = []

def display_menu() -> None:
    print("============= SECURITY LOG ANALYZER =============")
    print("1. Nhập và làm sạch dữ liệu Log thô")
    print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
    print("3. Mã hóa địa chỉ IP (Masking)")
    print("4. Đóng hệ thống")
    print("=================================================")

def clean_raw_logs(raw_input: str) -> list[str]:
    translation_table = str.maketrans("", "", "!@#$")
    cleaned_string = raw_input.translate(translation_table)
    return [log.strip() for log in cleaned_string.split(";") if log.strip()]

def load_and_clean_logs() -> None:
    global raw_logs

    print("--- NẠP DỮ LIỆU LOG ---")
    raw_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")
    raw_logs = clean_raw_logs(raw_input)
    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")

def filter_warning_logs(logs: list[str]) -> list[str]:
    return [
        log
        for log in logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]

def filter_alerts() -> None:
    global processed_logs

    print("--- LỌC CẢNH BÁO ---")

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    processed_logs = filter_warning_logs(raw_logs)
    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
    for log in processed_logs:
        print(f"- {log}")

def mask_ip_in_log(log_line: str) -> str:
    words = log_line.split()
    masked_words: list[str] = []

    for word in words:
        if "." in word:
            parts = word.split(".")
            if len(parts) == 4 and all(part.isdigit() for part in parts):
                masked_words.append(f"{parts[0]}.{parts[1]}.*.*")
                continue
        masked_words.append(word)

    return " ".join(masked_words)

def mask_ip_addresses(logs: list[str]) -> list[str]:
    return [mask_ip_in_log(log) for log in logs]

def mask_ips_report() -> None:
    print("--- MÃ HÓA IP ---")

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    masked_logs = mask_ip_addresses(processed_logs)
    print("Báo cáo log an toàn:")
    for index, log in enumerate(masked_logs, start=1):
        print(f"{index}. {log}")

def main() -> None:
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            load_and_clean_logs()
        elif choice == "2":
            filter_alerts()
        elif choice == "3":
            mask_ips_report()
        elif choice == "4":
            print("Hệ thống đã đóng. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()
