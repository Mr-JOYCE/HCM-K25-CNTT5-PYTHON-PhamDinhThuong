# Hệ thống đánh giá sĩ số lớp học cho mỗi chi nhánh và mỗi lớp
# Input/Output:
# - Input: số lượng chi nhánh (nguyên dương), và với mỗi chi nhánh 2 lần nhập số học viên đi học của từng lớp
# - Output: thông báo trạng thái lớp ngay sau khi nhập hợp lệ
# Giới hạn bài toán:
# - Mỗi chi nhánh có 2 lớp học
# - Số học viên phải là số nguyên >= 0
# - Nếu số học viên < 0 thì yêu cầu nhập lại
# - Nếu số học viên == 0 thì bỏ qua đánh giá trạng thái
# - Nếu số học viên >= 20 thì lớp ổn định
# - Nếu số học viên < 20 và > 0 thì lớp cần được nhắc nhở theo dõi


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Số lượng chi nhánh không hợp lệ. Vui lòng nhập lại.")
                continue
            return value
        except ValueError:
            print("Số lượng chi nhánh không hợp lệ. Vui lòng nhập lại.")


def read_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue
            return value
        except ValueError:
            print("Số học viên không hợp lệ. Vui lòng nhập lại.")


def evaluate_class(branch_number, class_number, attendance):
    if attendance == 0:
        print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
    elif attendance >= 20:
        print(f"Chi nhánh {branch_number} - Lớp {class_number}: Lớp học ổn định")
    else:
        print(f"Chi nhánh {branch_number} - Lớp {class_number}: Lớp cần được nhắc nhở theo dõi")


def main():
    branch_count = read_positive_int("Nhập số lượng chi nhánh: ")

    classes_per_branch = 2
    for branch_index in range(1, branch_count + 1):
        print(f"Chi nhánh {branch_index}:")
        for class_index in range(1, classes_per_branch + 1):
            attendance = read_non_negative_int(
                f"Nhập số học viên đi học của lớp {class_index}: "
            )
            evaluate_class(branch_index, class_index, attendance)


if __name__ == "__main__":
    main()
