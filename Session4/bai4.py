import random as rand

def main():
    exact_number = rand.randint(1, 99)
    count = 0
    while True:
        guess = int(input("Nhập một số bạn đoán từ 1 đến 100: "))
        if guess == exact_number:
            print(f"Chúc mừng! Bạn đã đoán đúng mã số may mắn {exact_number} sau {count} lần đoán.")
            print("--- TRÒ CHOI KẾT THÚC ---")
            break
        elif guess < exact_number:
            print("Gợi ý: Số bạn nhỏ hơn mã số may mắn!")
            count += 1
        else:           
            print("Gợi ý: Số bạn lớn hơn mã số may mắn!")
            count += 1
        if count >= 5:
            print(f"Bạn đã đoán quá 5 lần. Số chính xác là {exact_number}.")
            print("--- TRÒ CHOI KẾT THÚC ---")
            break

if __name__ == "__main__":
    main()