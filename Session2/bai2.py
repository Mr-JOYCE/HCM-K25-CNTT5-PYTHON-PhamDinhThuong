print("--- BLOOD DONATION ELIGIBILITY CHECK ---")

donor_age = int(input("Enter donor age: "))
donor_weight = int(input("Enter donor weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("ĐỦ ĐIỀU KIỆN")
else:
    reasons = []
    if donor_age < 18:
        reasons.append("Chưa đủ 18 tuổi")
    if donor_weight < 50:
        reasons.append("Cân nặng dưới 50 kg")

    if reasons:
        print("KHÔNG ĐỦ ĐIỀU KIỆN: " + "; ".join(reasons))
    else:
        print("KHÔNG ĐỦ ĐIỀU KIỆN")
