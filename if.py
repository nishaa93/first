Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=int(input("enter the number"))
enter the number 32
>>> if x<0:
	x=0
	print('negative change to zero')
	elif x==0:
		
SyntaxError: invalid syntax
>>> if x<0:
	x=0
	print('negative change to zero')
elif x == 0:
	print('zero')
elif x == 1:
	print('single')
else:
	print('more')

	
more
>>> words=['cat','window','door')
SyntaxError: invalid syntax
>>> words=['cat','window','door']
>>> for w in words:
	print(w,len(w))

	
cat 3
window 6
door 4
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> list=[0,1,2,3,5,6,7,8,9]
>>> list
[0, 1, 2, 3, 5, 6, 7, 8, 9]
>>> if list[0]==0;
SyntaxError: invalid syntax
>>> if list[0]==0:
	print("this number is zero")

	
this number is zero
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> range(3)
range(0, 3)
>>> for n in range(10):
	print(n)

	
0
1
2
3
4
5
6
7
8
9
>>> 
