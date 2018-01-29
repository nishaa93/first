Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> number=input("enter the number")
enter the number 12
>>> number
' 12'
>>> number=int(input("enter the number"))
enter the number12
>>> number
12
>>> number=string(input("enter the string"))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    number=string(input("enter the string"))
NameError: name 'string' is not defined
>>> number=str(input("enter the string"))
enter the stringnisha
>>> number
'nisha'
>>> number=str(input("enter the string"))
enter the string12
>>> number
'12'
>>> type(string)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    type(string)
NameError: name 'string' is not defined
>>> type(str)
<class 'type'>
>>> os.system('cls')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    os.system('cls')
NameError: name 'os' is not defined
>>> number=int(input("enter tyhe number"))
enter tyhe number12
>>> print("your number is ",number)
your number is  12
>>> name=input("what is your name")
what is your name nisha
>>> name
' nisha'
>>> regno=input("registration no.")
registration no.11615691
>>> course=input("course")
course MCA
>>> course
' MCA'
>>> print(name+regno+course)
 nisha11615691 MCA
>>> word=("hii i am happy")
>>> rwords=word[::-1]
>>> if word==rwords:
	print("string is palindrome")

	
>>> if word==rwords:
	print("your number is",number)
	else:
		
SyntaxError: invalid syntax
>>> word="hello i am happy"
>>> rwords=word[::-1]
>>> if word==rwords:
	print("string is palindrome")
	else:
		
SyntaxError: invalid syntax
>>> if word==rwords:
	print("string is palindrome")
else:
	print("both are equal")

	
both are equal
>>> 
