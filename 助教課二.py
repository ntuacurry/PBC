# 第一題

queen = input()
apple = int(input())

apple = apple - 1

if apple == 1:
    print("There is " + str(apple) + " apple in " + queen + "'s basket.")
else:
    print("There are " + str(apple) + " apples in " + queen + "'s basket.")
    
#第二題

name1 = input()
name2 = input()

print(name1 == name2)

#第三題

miles = float(input())

if miles <= 1:
    print("80.0")
elif miles <= 3:
    print("120.0")
else:
    price = 120 + (miles - 3) * 30
    print(float(price))
    
# 第四題

float1 = float(input())
float2 = float(input())
float3 = float(input())

if float1 > float2:
    if float1 > float3:
        print(float1)
    else:
        print(float3)
else:
    if float2 > float3:
        print(float2)
    else:
        print(float3)

# 第五題

dividend = int(input())
if dividend < 0:
    print("exit")
else:
    divisor = int(input())
    if divisor == 0:
        print("error")
    else:
        quotient = dividend // divisor
        remainder = dividend % divisor
        print(quotient, remainder, sep=",")