import random

CHOICES = {1: "kéo", 2: "búa", 3: "bao"}

def keo_bua_bao():
    print("1. Kéo")
    print("2. Búa")
    print("3. Bao")
    user = int(input("Chọn (1-3): "))
    ai = random.randint(1, 3)

    user_name = CHOICES[user]
    ai_name = CHOICES[ai]

    if user == ai:
        result = "Hoà"
    elif (user == 1 and ai == 3) or (user == 2 and ai == 1) or (user == 3 and ai == 2):
        result = "Bạn thắng"
    else:
        result = "AI thắng"

    print(f'Bạn chọn "{user_name}", AI chọn "{ai_name}" -> {result}')

def doan_so():
    target = random.randint(10, 99)
    while True:
        guess = int(input("Nhập số bạn đoán: "))
        if guess == target:
            print("Chúc mừng bạn đã đoán đúng")
            return
        print("Bạn đã đoán sai rồi")
        if guess < target:
            print("Số bạn đoán nhỏ hơn số cần đoán")
        else:
            print("Số bạn đoán lớn hơn số cần đoán")

def main():
    while True:
        choice = input("0. Thoát trò chơi\n1. Kéo búa bao\n2. Đoán số\nLựa chọn của bạn là: ")
        if choice == "0":
            break
        elif choice == "1":
            keo_bua_bao()
        elif choice == "2":
            doan_so()


if __name__ == "__main__":
    main()
