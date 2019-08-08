import math
def pizza():
    d = int(input(" diameter in inches\n:"))
    r = d // 2
    price = int(input(" price\n:"))
    area = float(3.14) * r**2
    final = price/area
    print("$",round(final, 2), "is the price/sq.in. of your pizza")

def volume():
    r = int(input("Please Enter a Radius\n :"))
    v = 4/(3*3.14*r**3)
    a = 4*3.14*(r**2)
    print(round(a, 2), "is surface area in sq.cm.", round(v, 2), "is volume in cubic centimeters")







def interest():
    count = 0
    rate = float(input("Input your interest rate (percentage)\n :"))
    principal = float(input("Input your principal\n :"))
    principal2 = float(input("Input principal a second time to confirm\n :"))
    if principal != principal2:
        raise ValueError('Principals do not match')
    limit = principal * 2
    ##calculate how much time during the year
    while principal <= limit:
        principal += principal*(rate/100)
        count += 1
    print(count,":The number of years until your investment doubles to",round(principal,2)







# def trianglearea():
#     a = float(input('Enter first side: '))
#     b = float(input('Enter second side: '))
#     c = float(input('Enter third side: '))
#     s = (a + b + c) / 2
#     area = (s*(s-a)*(s-b)*(s-c)) ** .5
#     print(round(area, 2), "Is the area of your triangle in inches")

interest()

# trianglearea()
# volume()
# pizza()
