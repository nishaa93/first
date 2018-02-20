Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number between",num1,",",num2,"and",num3,"is",largest)
SyntaxError: multiple statements found while compiling a single statement
>>> 
 RESTART: C:/Users/tnish/AppData/Local/Programs/Python/Python36-32/largest.py 
Enter first number: 32
Enter second number: 33
Enter third number: 45
The largest number between 32.0 , 33.0 and 45.0 is 45.0
>>> 
