Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> true==false
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    true==false
NameError: name 'true' is not defined
>>> True==False
False
>>> True==True
True
>>> def_is_prime(n):
	
SyntaxError: invalid syntax
>>> def is_prime(n)
SyntaxError: invalid syntax
>>> def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
		return True
	n=input("enter the number")
	x in range(2,int(n)):
		
SyntaxError: invalid syntax
>>> def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
		return True
	n=input("enter the number")
	for x in range(2,int(n)):
		if is_prime(x):
			print(x,"is prime")
		else:
			print(x,"is not prime")

			
>>> def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
		return True
	
	n=input("enter the number")
	for x in range(2,int(n)):
		if is_prime(x):
		   print(x,"is prime")
		else:
			print(x,"is not prime")

			
>>> 
========================== RESTART: G:/first/fun.py ==========================
>>> 
========================== RESTART: G:/first/fun.py ==========================
>>> 
========================== RESTART: G:/first/fun.py ==========================
enter the number 7def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
		return True

	n=input("enter the number")
	for x in range(2,int(n)):
		if is_prime(x):
		   print(x,"is prime")
		else:
			print(x,"is not prime")
