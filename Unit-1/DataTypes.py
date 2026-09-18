# 2. Data Types
# 1. Demonstrate int, float, str, bool, and complex.
a=10
print('int=',a)
b=10.2
print("float=",b)
c='Atmiya'
print('str=',c)
d=True
print('bool=',d)
e=10.5j
print('complext=',e)

# 2. Accept two numbers and display their data types.
num1=int(input("enter a value1="))
num2=int(input("enter a value2="))
print("type of num1=",type(num1))
print("type of num2=",type(num2))

# 3. Convert a string number into an integer and float.
num='123'
print("Before converion String number=",num)
print("after converion String number into Integer=",int(num))
print("after converion String number into float=",float(num))

# 4. Find the length of a string.
name="Atmiya"
print(name)
print("length of", name, "is", len(name))

# 5. Create a list, tuple, set, and dictionary and display their types.
l=[1,20,40,4]
t=(1,2,3,4,6,5)
s ={1.4, 3, 6, 7}
dis={"name":'Atmiya',"City":'Rajkot',"year":2020}
print(l)
print(t)
print(s)
print(dis)
print('--------------------------')
print(type(l))
print(type(t))
print(type(s))
print(type(dis))
