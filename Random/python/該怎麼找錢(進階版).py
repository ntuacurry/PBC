a = int(input())

b = (1000 - a) // 500 #b為500的張數
c = ((1000 - a) % 500) // 100 #c為100的張數
d = ((1000 - a) % 100) // 50  #d為50的個數
e = ((1000 - a) % 50) // 10 #e為10的個數
f = ((1000 - a) % 10) // 5 #f為5的個數
g = ((1000 - a) % 5) // 1 #g為1的個數

if b >= 1: #b是否不為0
 b1 = "500, " + str(b) + "; "
 if g == f == e == d == c == 0:
  b1 = "500, " + str(b)
else:
 b1 = ""

if c >= 1: #c是否不為0
 c1 = "100, " + str(c) + "; "
 if g == f == e == d == 0:
  c1 = "100, " + str(c)
else:
 c1 = ""

if d >= 1: #d是否不為0
 d1 = "50, " + str(d) + "; "
 if g == f == e == 0:
  d1 = "50, " + str(d)
else:
 d1 = ""

if e >= 1: #e是否不為0
 e1 = "10, " + str(e) + "; "
 if  g == f == 0:
  e1 = "10, " + str(e)
else:
 e1 = ""

if f >= 1: #f是否不為0
 f1 = "5, " + str(f) + "; "
 if  g == 0:
  f1 = "5, " + str(f)
else:
 f1 = ""

if g >= 1: #g是否不為0
 g1 = "1, " + str(g)
else:
 g1 = ""

print(b1 + c1 + d1 + e1 + f1 + g1)