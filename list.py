Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> new=["nisha",12,"female",24]
>>> new
['nisha', 12, 'female', 24]
>>> len(new)
4
>>> new[:3]
['nisha', 12, 'female']
>>> new[1:]
[12, 'female', 24]
>>> new[1:2:]
[12]
>>> list=[1,2,3,4,5,6,7,8,9,10]
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list[:10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list[1:]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list[1:2:]
[2]
>>> list[1:2:3]
[2]
>>> list[1:2:7]
[2]
>>> list[1:6:2]
[2, 4, 6]
>>> list[1:5:2]
[2, 4]
>>> n=[1,2,3,4,5,6]
>>> n1=[3,4,5,6,7,8]
>>> n+n1
[1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8]
>>> n3[1+2,2+3,3+4]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    n3[1+2,2+3,3+4]
NameError: name 'n3' is not defined
>>> n3=[1+2,2+3]
>>> n3
[3, 5]
>>> n4=[1-2,2-3,3-4]
>>> n4
[-1, -1, -1]
>>> 
