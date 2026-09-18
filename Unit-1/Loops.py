#1. Print numbers from 1 to 10 using a for loop.
for i in range(11):
    print(i)

#2. Print numbers from 10 to 1 using a while loop
i=10
while i>0:
    print(i)
    i-=1

#3. Print the multiplication table of a number.
num=int(input("enter a number"))
for i in range(1,11):
    print(num*i)

#4. Find the sum of numbers from 1 to n.
num=int(input("enter the number"))
sum=0
while num>0:
    sum+=num
    num-=1
print(sum)

#5. Find the factorial of a number.
num=int(input("enter a number"))
fac=1
while num>0:
    fac=fac*num
    num-=1
print(fac)

#6. Print all even numbers between 1 and 100.
for i in range(1,101):
    if(i%2==0):
        print(i,"is even number")
    else:
        print(i,"is odd number")

#7. Reverse a number using a loop.
num=int(input("enter a number="))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("revers number",rev)

#8. Count the digits of a number.
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits =", count)

#9. Check whether a number is prime.
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

#10. Print Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))=
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
