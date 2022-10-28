n = int(input())

food = []
ingredient_lst = []
for i in range(n):
    food_str = input().split(" ")
    food.append(food_str[0])
    ingredient = []
    for j in range(int(food_str[1])):
        ingredient.append(food_str[j + 2])
    ingredient_lst.append(ingredient)
dictionary = dict(zip(food, ingredient_lst))

m = int(input())
compare = []
for i in range(m):
    food_compare = input().split(" ")
    compare.append(food_compare)

for i in range(m):
    food_1 = dictionary[compare[i][0]]
    food_2 = dictionary[compare[i][1]]
    common_lst = []
    for j in range(len(food_1)):
        for k in range(len(food_2)):
            if food_1[j] == food_2[k]:
                common_lst.append(food_1[j])
    common_lst.sort()
    common = " ".join(common_lst)
    if common != "":
        print(common)
    else:
        print("nothing")