ref = input()
ref_List = ref.split()  # ref_List[0]是城鎮數 (測資組數)；[1]是基地台數；[2]是覆蓋半徑數

TownList = []

# 把所有城鎮的資料儲存進List中
for town_number in range(int(ref_List[0])):
    town = input()
    TownList.append(town.split())

bestTownList = []
people_final = 0

# 計算各基地台依序的位置
for site in range(int(ref_List[1])):
    maxPeople = 0
    bestTown = 0
    
# 計算各城鎮基地台覆蓋居民數量
    for town_number in range(int(ref_List[0])):
        people = 0
        bestTownSelected = []

        for town_another in range(int(ref_List[0])):
            distance = ((int(TownList[town_number][0]) - int(TownList[town_another][0])) ** 2 + (int(TownList[town_number][1]) - int(TownList[town_another][1])) ** 2) ** 0.5
            if distance <= int(ref_List[2]):
                people += int(TownList[town_another][2])
                bestTownSelected.append(town_another)
        if maxPeople < people:
            maxPeople = people
            bestTown = town_number + 1
            bestTownSelected_final = bestTownSelected

# 將有被選中的城鎮人數設為0
    for town_number in bestTownSelected_final:
        TownList[town_number][2] = 0
    bestTownList.append(bestTown)

    people_final += maxPeople

site = ""
for i in range(len(bestTownList)):
    site += str(bestTownList[i]) + " "

print(site + str(people_final))