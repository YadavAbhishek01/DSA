#4. Conditions

#1. Check whether a number is positive, negative, or zero.
a=10
print("given number",a)
if a>0:
    print("given number is positive")
elif a<0:
    print("given number is negative")
else:
    print("given number is zero")

#2. Check whethe******rson is eligible to vote.
age=1
print("age=",age)
if age>=18:
    print("you are eligible of voting")
else:
    print("You are not eligible for voting")

#3. Find the largest of three numbers.
a=10
b=20
c=15
print("value of a=",a)
print("value of b=",b)
print("value of c=",c)
if a>=b and a>=c:
    print("a is largest value")
elif b>=a and b>=c:
    print("b is largest value")
else:
    print("c is largest value")

#4. Check whether a year is a leap year.
year=2024
if year%4==0 or year%400==0:
    print("given year is loop year")
else:
    print("given year is not loop year")

#5. Create a grade system based on marks.
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

#6. Check whether a number is divisible by 5 and 11.
num = int(input("Enter your number: "))
if num%5==0 and num%11==0:
    print("given number is  divisible by 5 or 11")
else:
    print("given number is not divisible by 5 or 11")

#7. Create a simple calculator using if-elif-else.
num1 = int(input("Enter your  first number: "))
num2 = int(input("Enter your  second number: "))
symbole=input("Enter your  Symbole: ")
if symbole=="+":
           add=num1+num2
           print("addition of two number is=",add)
elif symbole=="-":
           sub=num1-num2
           print("subtraction of two number is=",sub)
elif symbole=="*":
           mul=num1*num2
           print("Multiplication of two number is=",mul)
elif symbole=="/":
           div=num1/num2
           print("division of two number is=",div)
else:
    print("invalid parametes")


