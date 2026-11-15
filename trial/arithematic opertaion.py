money = 3
#addition
#money = money + 1
#also written as money += 1, gives us same results(augmented assigned opperative of addtion)
#subtraction
#money = money - 2
#also written as money -= 2
#multiplication
#money = money * 3
#money *= 3 works too
#divison
#money = money / 3
#money /= 3
#exponents
#money = money ** 3 , read as number whole cube
#modulus- basically gives us a remainder upon divison of something
#money = money % 2
#helps in identification of odd and even
#print(money)



#uses of pow(), abs(), max(), min(), round()
x = 3.14
y = -7
z = 2
#round()- basically rounds up an float number to the nearest integer, but if it is round(x,2)- it is read as round of x variable to two digits
#result = round(x)
#abs()- absoulute function gives the value of a specific number as a distance away from origin, basically mod of number ig
#result = abs(y)
#pow(), basically power function given as (a,b), where a is the base number , b is the exponent
#result = pow(x,z)
#max(), min()- max/ min function gives the max/min value out of all the variable in the bracket
#result = max(x,y,z)
#sim for min
#print(result)

import math
#this basically allows us to use more functions
#result = math.pi- gives us pi value
#result = math.e - gives us e value
x = 9.1
#result = math.sqrt(x)- gives us sqr root
#result = math.ceil(x)- always rounds of to one higher integer, in this case 10
#result = math.floor(x)- always rounds of to one lower integer in this case 9
#print(result)


#ex 1- caluclate circumference of circle
#import math
#pi_value = math.pi
#radius = float(input("what is the radius of ur circle? :"))
#result = pi_value * radius * 2
#result = round(result)
#print(result)

#ex2: area of circle
#borrowing code from above ( radius code)
#area = math.pi * radius ** 2
#print(round(area,2))

#ex3: finding hypotenuse of right angles traingle
a = float(input("what is the length of side? :"))
b = float(input("what is the length of other side? :"))
a = a**2
b=b**2
c = a + b
c= math.sqrt(c)
print(f"the third side is {c} cm")

#or c = math.sqrt(pow(a,2) + pow(b,2))


