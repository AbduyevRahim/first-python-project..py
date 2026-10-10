# task 1
a = int(input("include any number: a="))
b = int(input("include anouther number: b="))
if a == b:
    print("Numbers are equal")
elif a > b:
    print("a greater than b")
else:
    print("b greater than a")



# task 2
a = int(input("include any number: "))
if a == 0:
    print("number is equal to zero")
elif a > 0:
    print("number is positive")
else:
    print("number is negative")



# task 3
a = int(input("include any number "))
if a % 2 == 0:
    print("number is even")
else:
    print("number is odd")



# task 4
a = int(input("inculude score "))
if a > 100 or a < 0:
    print("Invalid score")
elif a >= 91:
    print("A")
elif a >= 81:
    print("B")
elif a >= 71:
    print("C")
elif a >= 61:
    print("D")
elif a >= 51:
    print("E")
else:
    print("F")



# task 5
a = int(input("include any number: a="))
b = int(input("include another number: b="))
c = int(input("include another number: c="))
if a > b:
    if a > c:
        print("a is the largest number")
    elif a == c:
        print("largest number isn't exist")
    else:
        print("c is the largest number")
elif b > a:
    if b > c:
        print("b is the largest number")
    elif b == c:
        print("largest number isn't exist")
    else:
        print("c is the largest number")
else:
    print("largest number isn't exist")



# task 6
a = float(input("include any number "))
b = float(input("include antoher number "))
c = input("include operation like(+,-,*,**,/,//,%) ")
if c == "+":
    print("result", a + b)
elif c == "-":
    print("result", a - b)
elif c == "*":
    print("result", a * b)
elif c == "**":
    print("result", a ** b)
elif c == "/":
    if b == 0:
        print("cannot divide by zero")
    else:
        print("result", a / b)
elif c == "//":
    if b == 0:
        print("cannot divide by zero")
    else:
        print("result", a // b)
elif c == "%":
    if b == 0:
        print("cannot divide by zero")
    else:
        print("result", a % b)
else:
    print("doesn't exist operation like that")



# task 7
a = int(input("include your age "))
if a <= 12 and a >= 0:
    print("you are a child")
elif a <= 17 and a >= 13:
    print("you are a teenager")
elif a <= 64 and a >= 18:
    print("you are an adult")
elif a >= 65:
    print("you are a senior")
else:
    print("invalid age")



# task 8
a = int(input("total purchase amount "))
if a < 100:
    print("no discount")
elif a <= 299 and a >= 100:
    b = a * 10 / 100
    print("you got 10% discount. Discount amount", b, "AZN. Result", a - b, "AZN")
elif a <= 499 and a >= 300:
    b = a * 15 / 100
    print("you got 15% discount. Discount amount", b, "AZN. Result", a - b, "AZN")
else:
    b = a * 20 / 100
    print("you got 20% discount. Discount amount", b, "AZN. Result", a - b, "AZN")



# task 9
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    if b > c and b != c:
        print("the largest number is", a, "and the smallest is", c)
    elif c > b and c != b:
        print("the largest number is", a, "and the smallest is", b)
    else:
        print("the largest and smallest numbers aren't exist or some of them are equal")
elif b > a and b > c:
    if a > c and a != c:
        print("the largest number is", b, "and the smallest is", c)
    elif c > a and c != a:
        print("the largest number is", b, "and the smallest is", a)
    else:
        print("the largest and smallest numbers aren't exist or some of them are equal")
else:
    if b > a and b != a:
        print("the largest number is", c, "and smallest number is", a)
    elif a > b and a != b:
        print("the largest number is", c, "and smallest number is", b)
    else:
        print("the largest and smallest numbers aren't exist or some of them are equal")



# task 10
a = 1000
b = int(input("the amount you want to withdraw "))
if b == 0 and b < 0:
    print("Invalid amount")
elif b > a:
    print("Insufficient balance")
else:
    c = a - b
    print("remain amount=", c)



# task 11
a = float(input("include your monthly electricity usage"))
if a <= 100 and a >= 0:
    b = a * 0.08
    print("usage:", a, "kWh Applied rate: 0.08 AZN Total bill:", b, "AZN")
elif a <= 300 and a >= 101:
    b = a * 0.12
    print("usage:", a, "kWh Applied rate: 0.12 AZN Total bill:", b, "AZN")
elif a > 300:
    b = a * 0.15
    print("usage:", a, "kWh Applied rate: 0.15 AZN Total bill:", b, "AZN")
else:
    print("invalid input")



# task 12
a = 2.0
b = float(input("include your distance with km "))
if b <= 5 and b >= 0:
    c = b * 0.70
    print("starting fee:2 AZN Distance fee:", c, "AZN/km Total amount:", a + c, "AZN")
elif b <= 15 and b >= 5:
    c = b * 0.60
    print("starting fee:2 AZN Distance fee:", c, "AZN/km Total amount:", a + c, "AZN")
elif b > 15:
    c = b * 0.50
    print("starting fee:2 AZN Distance fee:", c, "AZN/km Total amount:", a + c, "AZN")
else:
    print("invalid fee")



# task 13
a = int(input("include your age "))
b = float(input("include your salary "))
c = float(input("include your requested loan amount "))
if a < 18:
    print("requested loan is rejected because your are young")
elif b < 500:
    if c > b * 10:
        print("loan is rejected because requested loan is more than ten times your salary")
    else:
        print("requested loan is rejected because your salary isn't enough")
else:
    print("requested loan is approved")



# task 14
a = int(input("include the one of the triangle sides "))
b = int(input("include an another triangle side "))
c = int(input("include a last side of the triangle "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b:
                if b == c:
                    print("Equilateral")
                else:
                    print("Isoscales")
            elif b == c:
                if a == b:
                    print("Equilateral")
                else:
                    print("Isoscales")
            elif a == c:
                if c == b:
                    print("Equilateral")
                else:
                    print("Isoscales")
            else:
                print("Scalene")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")
else:
    print("Triangle cannot be created")



# task 15
a = float(input("include your exam score. that must be between 0-700: "))
b = float(input("include your school score. that must be between 0-100: "))
c = int(input("include your age: "))
if c < 16:
    print("application is rejected because you are young")
elif a >= 600:
    print("application is accepted with a scholarship")
elif a <= 599 and a >= 450:
    print("application is accepted")
elif a <= 449 and a >= 300:
    if b >= 80:
        print("application is accepted")
    else:
        print("application is rejected because your school score isn't enough")
else:
    print("application is rejected because your exam score isn't enough")