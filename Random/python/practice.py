c = int(input()) #進貨成本
r = int(input()) #零售價
N = int(input()) #可能的需求數
p0 = float(input())
p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())
p6 = float(input())
p7 = float(input())
p8 = float(input())

# n = 0 #最佳訂購量q，初始值先設為0
# totalProfit = 0
m = 0


for n in range(0, N + 1):
 i = 0
 totalP = 0
 totalProfit = 0
 for p in p0, p1, p2, p3, p4, p5, p6, p7, p8:
  while i < n: 
   profit = (i * r - c * n) * p #利潤
   i += 1
   break
  else:
   break
  totalProfit = totalProfit + profit #加權後的利潤加總
  totalP = totalP + p #機率的累積
 totalProfit = totalProfit + (r - c) * n * (1 - totalP)
 if m < totalProfit:
  m = totalProfit
 if m > totalProfit:
  break
print(n - 1, int(m))


