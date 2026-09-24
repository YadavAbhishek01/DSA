#1.Write a function to print "Hello, World!".
def msg():
    print("Hello,World")
msg()
#2.Write a function that takes a name and prints a greeting.
def greetmsg():
    name=input("enter a name=")
    print("Welcome",name)
greetmsg()

#3.Write a function to add two numbers.
def sum():
    num1=int(input("enter a num="))
    num2=int(input("enter second num="))
    add=num1+num2
    print("Addition of two numbers=",add)
sum()

#4.Write a function to find the square of a number.
def squre():
    num=int(input("enter number="))
    sqr=num*num
    print("given number squre is=",sqr)
squre()

#5.Write a function to check whether a number is even or odd.
def even():
    num=int(input("enter number="))
    if num%2==0:
        print("given number is even")
    else:
        print("given number is odd")
even()
#6.Write a function to find the maximum of two numbers.
def max():
    num1=int(input("enter number="))
    num2=int(input("enter number2="))
    if num1>num2:
        print(num1,'is maximum number')
    else:
        print(num2,'is maximum number')
max()
#7.Write a function to convert Celsius to Fahrenheit.
def fahrenheit():
    cel=int(input("enter a celsius="))
    f=(cel*9/5)+32
    print("Fahrenheit=",f)
fahrenheit()
#8.Write a function to calculate the area of a circle.
def circle():
    r=int(input("enter a radius="))
    pie=3.14
    area=pie*r*r
    print("area of circle is =",area)
circle()
#9.Write a function to calculate the factorial of a number.
def factorial():
    num=int(input("enter a number="))
    fact=1
    while num>0:
        fact=fact*num 
        num-=1
        print(fact)
factorial()
#10.Write a function to check whether a number is positive, negative, or zero.
def positive():
    no=int(input("enter a number="))
    if no>0:
        print(no,"given number is positive")
    elif no==0:
        print(no,"given number is zero")
    else:
        print(no,"given number is negative")
positive()
#11.Write a function to find the maximum of three numbers.
print('----------------------------------------------------')
print("Write a function to find the maximum of three numbers.")
def max():
    a=int(input("enter 1 number="))
    b=int(input("enter 2 number="))
    c=int(input("enter 3 number="))
    if a>b and a>c:
        print(a,"is a maxium value")
    elif b>a and b>c:
        print(b,"is a maxium value")
    else:
        print(c,"is a maxium value")
max()
#12.Write a function to count vowels in a string.
print('----------------------------------------------------')
print("Write a function to count vowels in a string..")
def vowel():
    s="Atmiya University"
    count=0
    vowel=['a','e','i','o','u']
    for i in range(len(s)):
        print(s[i])
        if(s[i] in vowel):
            count +=1
    print("count of vowel",count)
vowel()
#13.Write a function to reverse a string.
def revers():
    a=input("enter a string=")
    print(a[::-1])
revers()
#14.Write a function to check whether a string is a palindrome.
def is_palindrome():
    a = input("Enter a string value = ")
    return a == a[::-1]

if is_palindrome():
    print("Palindrome")
else:
    print("Not palindrome")

#15.Write a function to find the sum of all elements in a list.
def total():
    l=[1,2,3,4,5]
    print("list=",l)
    for i in range(len(l)):
        ans=sum(l)
        return ans

print("sum of values=",total())

#16.Write a function to find the largest element in a list.
def largest():
    li=[1,2,3,4,5]
    ans=li[0]
    for i in range(len(li)):
        if i >ans:
            ans=i
    return ans
print(largest())
#17.Write a function to remove duplicate elements from a list.
def remove():
    li=[1,2,2,3,3,4]
    print(list(set(li)))
remove()
#18.Write a function to count how many times an element appears in a list.
def find(element):
    li=[1,2,2,3,4,4,5]
    count=0
    for i in range(len(li)):
        if li[i]==element:
            count+=1
    return count

print(find(2))
#19.Write a function to check whether a number is prime.
import math
def Prime():
    no=int(input("enter a number="))
    prime=True
    if no<=1:
        prime=False
    else:
        for i in range(2,no):
            if no%i==0:
                prime=False
            
    if prime:
        print(no,'given number is  prime')
    else:
        print(no,'given number is not prime')

Prime()

#20.Write a function to return all prime numbers between two numbers.
def Prime():
    no1=int(input("enter a first number="))
    no2=int(input("enter a second number"))
  

    if no1<=1 or no2<=1:
        prime=False
    else:
        for i in range(no1,no2):
            prime=True
            for j in range(2,i):
                if i%j == 0:
                    prime=False
                
            if prime:
                print(i,"this are numbers is prime")
            else:
                print(i,"this are not numbers is prime")

Prime()
#21.Write a function to calculate Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    result = []

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result

print(fibonacci(10))

#22.Write a function to find the second-largest number in a list.
def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    largest = max(unique_numbers)
    unique_numbers.remove(largest)

    return max(unique_numbers)

print(second_largest([10, 20, 5, 30, 25]))

#23.Write a function to sort a list without using sort().
def sort_list(numbers):
    result = numbers.copy()

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    return result

print(sort_list([5, 2, 8, 1, 3]))

#24.Write a function to merge two lists and remove duplicates.
def merge_remove_duplicates(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result

print(merge_remove_duplicates([1, 2, 3], [2, 3, 4, 5]))