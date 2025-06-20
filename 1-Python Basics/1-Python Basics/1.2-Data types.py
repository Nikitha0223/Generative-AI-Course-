#Data types
#Convert a string to an integer and perform arithmetic operations.
n_str="2"
n=int(n_str)
#arthimetic operations
n_sum=n+1
n_sub=n-1
n_mul=n*2
n_div=n/2
print("Addition :",n_sum,"\nSubtraction :",n_sub,"\nMultiplication :",n_mul,"\nDivision :" ,n_div)
#formatted way
print(f"\nAddition : {n_sum} \nSubtraction : {n_sub} \nMultiplication : {n_mul} \nDivision : {n_div}")
#output
Addition : 3 
Subtraction : 1 
Multiplication : 4 
Division : 1.0

Addition : 3 
Subtraction : 1 
Multiplication : 4 
Division : 1.0

#Store a float, string, integer, and list in variables and print their types.
a=1.0
b="Nikitha"
c=2
d=[1, 2, 3, 4]
print(f"Float : {a} {type(a)}\n"
    f"String : {b} {type(b)}\n"
    f"Integer : {c} {type(c)}\n"
    f"List : {d} {type(d)}")
#output
Float : 1.0 <class 'float'>
String : Nikitha <class 'str'>
Integer : 2 <class 'int'>
List : [1, 2, 3, 4] <class 'list'>

#Create a list of your favorite tech stacks and print them one by one using a loop.
stacks=["Sap abap + Sap hana" , "React js + Node js" , "Artificial Intelligence"]
print("My favorite tech stacks :")
for i in stacks:
    print("- " + i)
#Output
My favorite tech stacks :
- Sap abap + Sap hana
- React js + Node js
- Artificial Intelligence

#Write a Python script to count the number of vowels in a given string.
text=input("Enter the text :")
vowels = "aeiouAEIOU"
count=0
for v in text:
    if v in vowels:
        count += 1
print("The vowels in the given text :",count)
#Output
Enter the text :hello world&
The vowels in the given text : 3

1. Integer and Float
a = 10
b = 3.14
print(type(a))
print(type(b))
Output:
<class 'int'>
<class 'float'>

2. String
name = "Python"
print(type(name))
print("Welcome to", name)
Output:
<class 'str'>
Welcome to Python

3. Boolean
is_ai_fun = True
print(type(is_ai_fun))
print("Is AI fun?", is_ai_fun)
Output:
<class 'bool'>
Is AI fun? True

4. List
fruits = ["apple", "banana", "cherry"]
print(type(fruits))
print("First fruit:", fruits[0])
Output:
<class 'list'>
First fruit: apple

5. Tuple
coordinates = (10, 20)
print(type(coordinates))
print("X value:", coordinates[0])
Output:
<class 'tuple'>
X value: 10

6. Dictionary
student = {"name": "Alice", "age": 21}
print(type(student))
print("Student Name:", student["name"])
Output:
<class 'dict'>
Student Name: Alice

7. Set
unique_nums = {1, 2, 3, 3, 2}
print(type(unique_nums))
print(unique_nums)
Output:
<class 'set'>
{1, 2, 3}

