class Card:
    def __init__(self, suit, rank):  # suit是花色，rank是點數
        self.suit = suit
        if rank == "A":
            rank = 1
        elif rank == "J":
            rank = 11
        elif rank == "Q":
            rank = 12
        elif rank == "K":
            rank = 13
        self.rank = int(rank)
    
    # 判斷是否有A
    def hasA(self):
        if self.rank == 1:
            return True
        else:
            return False
    def isPairWith(self, aCard):
        if self.rank == aCard.rank:
            return True
        else:
            return False

color = input().split(",")
number = input().split(",")

card1 = Card(color[0], number[0])
card2 = Card(color[1], number[1])
card3 = Card(color[2], number[2])
card4 = Card(color[3], number[3])
card5 = Card(color[4], number[4])

card_lst = [card1, card2, card3, card4, card5]
score = 0
# 是否有A
for i in range(5):
    if card_lst[i].hasA():
        score += 5
# 是否有一對
for i in range(5):
    for j in range(i + 1, 5):
        if card_lst[i].isPairWith(card_lst[j]):
            score += 10

# 是否五張同花
for i in range(4):
    if card_lst[i].suit != card_lst[i + 1].suit:
        break
    else:
        if i == 3:
            score += 30

# 是否為順子
num_lst = []
for card in card_lst:
    num_lst.append(card.rank)
num_lst.sort()
for i in range(4):
    if num_lst == [1, 10, 11, 12, 13] or num_lst == [1, 2, 11, 12, 13] \
        or num_lst == [1, 2, 3, 12, 13] or num_lst == [1, 2, 3, 4, 13]:
        score += 50
        break
    elif num_lst[i] != num_lst[i + 1] - 1:
        break
    else:
        if i == 3:
            score += 50

# 是否為葫蘆
rank_dict = dict()
for i in range(5):
    if card_lst[i].rank not in rank_dict:
        rank_dict[card_lst[i].rank] = 1
    else:
        rank_dict[card_lst[i].rank] += 1
fullhouse = list(rank_dict.values())
if fullhouse == [3, 2] or fullhouse == [2, 3]:
    score += 80

# 是否為四條
if fullhouse == [4, 1] or fullhouse == [1, 4]:
    score += 100

# 是否為同花順
suit_dict = dict()
for i in range(5):
    if card_lst[i].suit not in suit_dict:
        suit_dict[card_lst[i].suit] = [card_lst[i].rank]
    else:
        suit_dict[card_lst[i].suit].append(card_lst[i].rank)
combo = list(suit_dict.values())
if len(combo) == 1:
    straightFlush = combo[0]
    straightFlush.sort()
    for i in range(4):
        if straightFlush == [1, 10, 11, 12, 13] or straightFlush == [1, 2, 11, 12, 13] \
            or straightFlush == [1, 2, 3, 12, 13] or straightFlush == [1, 2, 3, 4,13]:
            score += 300
            break    
        elif straightFlush[i] != straightFlush[i + 1] - 1:
            break
        else:
            if i == 3:
                score += 300

print(score)