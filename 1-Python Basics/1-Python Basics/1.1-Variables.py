#Variables 
#Take input from the user for name and age, store them in variables, and print a formatted introduction.
name = str(input("Enter the name :"))
age = int(input("Enter the age :"))
print("My name is" , name , "and I am" , age , "years old!")
print(f"Hello, my name is {name} and I am {age} years old!")
#Output
Enter the name :nikki
Enter the age :24
My name is nikki and I am 24 years old!
Hello, my name is nikki and I am 24 years old!

#Swap two variables using a temporary variable.
a=1
b=2
temp=a
a=b
b=temp
print(a)
print(b)
#output
2
1

#Swap two variables without using a third variable.
a=1
b=2
a=a+b
b=a-b
a=a-b
print("a :",a)
print("b :",b)
#output
a : 2
b : 1

#Assign a value to a variable and check its data type using type().
a=1
print(type(a))
a='Nikki'
print(type(a))
