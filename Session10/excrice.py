def main():
    numbers = [45, 12, 87, 34, 91, 56, 23, 78, 11, 69, 4, 38, 95, 27, 62, 15, 83, 50, 7, 41]
    #numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    check = 0

    # Dùng thuật toán Bubble Sort tăng dần
    #for i in range(len(numbers)):
    #    for j in range(0, len(numbers) - i - 1):
    #       if numbers[j] > numbers[j + 1]:
    #           numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    #Dùng thuất toán Bubble Sort giảm dần
    # for i in range(len(numbers)):
    #     for j in range(0, len(numbers) - i - 1):
    #         if numbers[j] < numbers[j + 1]:
    #             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Dùng thuật toán Insertion Sort tăng dần kiểm tra đã xắp xếp chưa
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
        if j + 1 != i:
            check = 1
    if check == 0:
        print("Danh sách đã được sắp xếp.")

    # Dùng thuật toán Insertion Sort giảm dần kiểm tra đã xắp xếp chưa
    # for i in range(1, len(numbers)):
    #     key = numbers[i]
    #     j = i - 1
    #     while j >= 0 and numbers[j] < key:
    #         numbers[j + 1] = numbers[j]
    #         j -= 1
    #     numbers[j + 1] = key
    #     if j + 1 != i:
    #         check = 1
    # if check == 0:
    #     print("Danh sách đã được sắp xếp.")


    print("Danh sách sau khi sắp xếp:", numbers)

if __name__ == "__main__":
    main()