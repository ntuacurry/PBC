FFM = float(input("請輸入除脂體重："))
BMR = int(input("請輸入基礎代謝率："))

TDEE = BMR / 0.7
protein = FFM * 2.2
fat1 = FFM * 0.6
fat2 = FFM * 1.2
carbohydrate1 = (TDEE - protein * 4 - fat1 * 9) / 4
carbohydrate2 = (TDEE - protein * 4 - fat2 * 9) / 4

fat3 = (TDEE - protein * 4 - 50 * 4)/9

print("")
print("高碳日:", "\n", "蛋白質：" + str(round(protein, 2)) + " " + "脂肪：" + str(fat1) + "~" + str(fat2) + " " + "碳水化合物：" + str(round(carbohydrate2, 2)) + "~" + str(round(carbohydrate1, 2)))
print("")
print("\n低碳日:", "\n", "蛋白質：" + str(round(protein, 2)) + " " + "脂肪：>= " + str(round(fat3, 2)) + " " +  "碳水化合物：< 50")