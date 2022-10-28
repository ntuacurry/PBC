c = int(input()) #進貨價格
r = int(input()) #零售價
N = int(input()) #需求的可能個數8
q = int(input()) #訂貨量
p0 = float(input())
p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())
p6 = float(input())
p7 = float(input())
p8 = float(input())
i = 0
profit = 0 
totalProfit = 0
totalP = 0

for p in p0, p1, p2, p3, p4, p5, p6, p7, p8:
 while i < q: #不知道為甚麼要加一
  profit = (i * r - c * q) * p #利潤
  i += 1
  break
 else:
  break
 totalProfit = totalProfit + profit #加權後的利潤加總
 totalP = totalP + p #機率的累積 

totalProfit = totalProfit + q * (r - c) * (1 - totalP)
print(int(totalProfit))