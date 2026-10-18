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



#task 16
a=int(input("include exam score "))
if a<0 or a>100:
	print("application is rejected")
else:
	x="pass" if a>=51 else "fail"
	print(x)



#task 17
a=float(input("order total "))
b=input("membership answer (yes or no): ")
if b!="no" and b!="yes" or a<0:
	print("delivery is rejected")
else:
	x=(f"delivery is free, total amount is {a} AZN") if a<50 or b=="yes" else (f"delivery cost is 5 AZN, total amount is {a+5} AZN")
	print(x)

   

#task 18
day=int(input("include day "))
match day:
	case 1:
		print("Monday, studyday")
	case 2:
		print("Tuesday, studyday")
	case 3:
		print("Wednesday, studyday")
	case 4:
		print("Thursday, studyday")
	case 5:
		print("Friday, studyday")
	case 6:
		print("Saturday, weekend")
	case 7:
		print("Sunday, weekend")
	case _:
		print("invalid day")



  #task 19
a = input("include drink code: T = Tea (2 AZN), C = Coffee (4 AZN), J = Juice (3 AZN): ")
b = int(input("include drink quantity(1-10): "))
if b>10 or b<=0:
    print("invalid")
else:
    match a:
        case "T":
            x = "larger order" if 2 * b > 20 else "regular order"
            print(f"Tea, Quantity:{b}, Total:{b * 2}AZN")
            print(x)
        case "C":
            print(f"Coffee, Quantity:{b}, Total:{b * 4}AZN")
            x = "larger order" if 4 * b > 20 else "regular order"
            print(x)
        case "J":
            print(f"Juice, Quantity:{b}, Total:{b * 3}AZN")
            x = "larger order" if 3 * b > 20 else "regular order"
            print(x)
        case _:
            print("invalid")



 #task 20
a=input("include your id(it must have 8 digits and you only use these numbers(0-9)) ")
if a.isdecimal() and a.isascii() and len(a)==8:
	print("Student ID accepted")
else:
	print("id is invalid")



#task 21
PIN="0325"
a=input("include your pin code ")
if len(a)>0:
	if len(a)==4:
		if a.isdecimal() and a.isascii():
			if a==PIN:
				print("Access granted")
			else:
				print("incorrect PIN")
		else:
			print("Digits only")
	else:
		print("PIN must have 4 digits")
else:
	print("PIN is required")



#task 22
a=input("include your phone number: ")
if len(a)==10:
	if a[0]=="0":
		if a.isdecimal() and a.isascii():
			b=a[0:3]
			match b:
				case "050"|"051"|"055"|"070"|"077"|"099":
					print("phone number accepted")
				case _:
					print("first applicable error")
		else:
			print("you can use only digits")
	else:
		print("your phone number must start zero")
else:
	print("your phone number must be 10 digits")



#task 23
Balance=1000
Pin="0437"
a=input("include your PIN: ")
b=input("include withdrawal amount: ")
if len(a)!=4 or not (a.isdecimal() and a.isascii()):
	print("Pin code must be 4 digits. you can use only digits")
elif a==Pin:
	if not (b.isdecimal() and b.isascii()):
		print("amount format error")
	elif int(b)>1000:
		print("available amount error")
	elif int(b)<10 or int(b)>500 :
		print("amount range error")
	elif int(b)%10!=0:
		print("banknote rule error")
	else:
		x=("0") if int(b)<=200 else ("2")
		if int(x)+int(b)>1000:
			print("application is rejected")
		else:
			print(f"withdrawal amount:, {int(b)}, fee service:, {x}, new balance:, {1000-(int(b)+int(x))}")
else:
	print("your PIN is incorrect")



#task 24
a=input("include product code you can use:K = Keyboard (40 AZN), M = Mouse (20 AZN), H = Headphones (60 AZN): ")
b=input("include quantitiy(that must be (1-5)): ")
c=input("include cupon code(SAVE10 or NONE): ")
d=input("include delivery code(P = Pickup (free), S = Standard): ")
match a:
	case "K":
		s=40*int(b) #s is subtotal
		print(f"product: Keyboard (40AZN). Subtotal: {40*int(b)} AZN")
	case "M":
		s=20*int(b)
		print(f"product: Mouse (20AZN). Subtotal: {20*int(b)} AZN")
	case "H":
		s=60*int(b)
		print(f"product: Headphones(60AZN). Subtotal: {60*int(b)} AZN")
	case _:
		print("invalid product")
		exit()
if not (b.isdecimal() and b.isascii()) or len(b)==0:
	print("only one digit and you can use")
	exit()
elif not (int(b)<=5 and int(b)>=1):
	print("you can use one digit between 1-5")
	exit()	
elif c=="SAVE10"or c=="NONE":
	if c=="SAVE10" and s>=100:
		ds=s-(s*10/100) #ds is discounted subtotal
		print(f"Kupon: SAVE10. Discount: {s*10/100} AZN. Subtotal: {ds} AZN")
	else:
		ds=s
		print("Discount is none")
else:
	print("Invalid cupon code")
	exit()
match d:
	case "P":
		print("Delivery code: Pickup. Delivery is free")
	case "S":
		x=(f"Delivery code: Standart. Delivery: 5 AZN. Subtotal:{ds+5} AZN") if ds<80 else ("Delivery code: Standart. Delivery is free")
		print(x)
	case _:
		print("Invalid delivery code")
		exit()



#task 25
a=input("include your student ID: ")
b=input("include your age: ")
c=input("include your workshop code(PY=Python(min age 16), WEB=WEB development(min age 16), CY=Cybersecurity(min age 18)): ")
d=input("include payment amount: ")
if not (a.isdecimal() and a.isascii()) or len(a)!=8:
	print("Your ID is incorrect")
else:
	print("Your ID is correct")
	if not (b.isdecimal() and b.isascii()):
		print("Your age is invalid")
	else:
		b=int(b)
		if not (b>=16 and b<=65):
			print("Invalid age")
		else:
			print(f"age: {b}")
			match c:
				case "PY":
					print("Workshop= PY")
				case "WEB":
					print("Workshop= WEB")				
				case "CY":
					x="your age isn't enough" if b<18 else "Workshop= CY"
					print(x)		
				case _:
					print("Code is rejected")
					exit()
if not d.isdecimal() and d.isascii():
	print("Invalid payment")
else:
	print(f"Payment= {d} AZN")
	if b<=18 and b>=16:
		d=int(d)
		if c=="PY":
			if d<(30-(d*20/100)):
				print("Expected= Insufficient payment")
			else:
				print("Expected= Registration confirmed")
				print(f"Discount= {d*20/100} AZN")
				print(f"Final fee= {30-(d*20/100)} AZN")
				print(f"Change= {30-(30-(d*20/100))} AZN")
		elif c=="WEB":
			if d<(40-(d*20/100)):
				print("Expected= Insufficient payment")
			else:
				print("Expected= Registration confirmed")
				print(f"Discount= {d*20/100} AZN")
				print(f"Final fee= {40-(d*20/100)} AZN")
				print(f"Change= {40-(40-(d*20/100))} AZN")
		elif c=="CY":
			if b==18:
				if d<(50-(d*20/100)):
					print("Expected= Insufficient payment")
				else:
					print("Expected= Registration confirmed")
					print(f"Discount= {d*20/100} AZN")
					print(f"Final fee= {50-(d*20/100)} AZN")
					print(f"Change= {50-(50-(d*20/100))} AZN")
			else:
				print("Invalid age")

