
#Conditional statements
# Write a program to check whether a number is positive, negative, or zero.
n=int(input("Enter the number: "))
if n==0:
    print("The given number is zero")
elif n>0:
    print("The given number is positive")
else:
    print("The given number is negative")
#Output
Enter the number: -4
The given number is negative

#Build a program that takes a score and returns a grade:90+ = A, 80–89 = B, 70–79 = C, 60–69 = D, <60 = F
a=int(input("Enter the score : "))
if a > 90:
    print("The grade is A")
elif a<90 and a>80:
    print("The grade is B")
elif a<80 and a>70:
    print("The grade is C")
elif a<70 and a>60:
    print("The grade is D")
else:
    print("The grade is F")
#Output
Enter the score : 62
The grade is D

#Write a simple login system that validates username and password.
username="Nikitha"
password="Veer@2724"
user=str(input("Enter the username : "))
passw=str(input("Enter the password : "))
if username==user and password==passw:
    print("The credentials are correct and you may logged in!")
else:
    print("Invalid Input!")
#Output
Enter the username : Nikitha
Enter the password : Veer@2724
The credentials are correct and you may logged in!
