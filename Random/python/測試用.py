i = 0
q = int(input())
profit = 0

for n in range(0,3):
 while i < q:
  profit = i * n
  i += 1
  break
 print(profit)

# N = int(input()) 
# m = 0
# n = 0
# i = 0
# profit = 0

# while n <= N:
 # for p in range(0, 3):
  # while i < N:
   # profit = i * p
   # i += 1
   # break
  # m = m + profit
 # n +=1 
 # print(m)
 # continue