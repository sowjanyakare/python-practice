Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2u='i am sowjanya'
SyntaxError: invalid syntax
>>> python class='hi'
SyntaxError: invalid syntax
>>> m name='hello'
SyntaxError: invalid syntax
>>> s='hello'
>>>  s='hello'
 
SyntaxError: unexpected indent
>>> to_u=065
SyntaxError: invalid token
>>> to_u=65
>>> t0_u
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t0_u
NameError: name 't0_u' is not defined
>>> to_u
65
>>> to-u=78
SyntaxError: can't assign to operator
>>> to@e=67
SyntaxError: can't assign to operator
>>> var1=var2=var3=60
>>> var1
60
>>> var2
60
>>> var3
60
>>> name,rollno,branch='sowjanya',65,'CME'
>>> name
'sowjanya'
>>> rollno
65
>>> branch
'CME'
>>> print(name)
sowjanya
>>> m=65,n=81
SyntaxError: can't assign to literal
>>> m,n=65,81
>>> p=m
>>> m=n
>>> n=p
>>> m
81
>>> n
65
>>> #without using temporary variable
>>> p,q=100,65
>>> p=p+q
>>> q=p-q
>>> p=p-q
>>> p
65
>>> q
100
>>> 
===== RESTART: C:\Users\HP\Desktop\project\python practice\day2-file2.py =====
hello world
before swaping 20 30
after swaping 20 20
>>> 
===== RESTART: C:\Users\HP\Desktop\project\python practice\day2-file2.py =====
hello world
before swaping 20 30
after swaping 30 20
>>> 
===== RESTART: C:\Users\HP\Desktop\project\python practice\day2-file2.py =====
hello world
before swaping 90 70
after swaping 70 90
>>> 
===== RESTART: C:\Users\HP\Desktop\project\python practice\day2-file2.py =====
hello world
before swaping 78 100
after swaping 100 78
>>> a=10
>>> type(a)
<class 'int'>
>>> a=1234567891234567891234567890
>>> type(a)
<class 'int'>
>>> f=123445566778.13243546576879808978867
>>> type(f)
<class 'float'>
>>> 
>>> 
>>> 
>>> 
>>> c='a'
>>> type(a\c)
SyntaxError: unexpected character after line continuation character
>>> type(c)
<class 'str'>
>>> name="s"
>>> type(s)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    type(s)
NameError: name 's' is not defined
>>> type(name)
<class 'str'>
>>> c=True
>>> type(c)
<class 'bool'>
>>> c=true
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    c=true
NameError: name 'true' is not defined
>>> c=i+j1
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    c=i+j1
NameError: name 'i' is not defined
>>> c=3+4k
SyntaxError: invalid syntax
>>> v=1+2j
>>> type(v)
<class 'complex'>
>>> 
===== RESTART: C:/Users/HP/Desktop/project/python practice/day2-file3.py =====
<class 'int'>
>>> 
===== RESTART: C:/Users/HP/Desktop/project/python practice/day2-file3.py =====
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/project/python practice/day2-file3.py", line 2, in <module>
    print(type(val))
NameError: name 'val' is not defined
>>> 
===== RESTART: C:/Users/HP/Desktop/project/python practice/day2-file3.py =====
enter a value23
<class 'str'>
>>> 
===== RESTART: C:/Users/HP/Desktop/project/python practice/day2-file3.py =====
enter a value: 12
enter b value: 13
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/project/python practice/day2-file3.py", line 4, in <module>
    print(a,b,type(a,b))
TypeError: type() takes 1 or 3 arguments
>>> 
===== RESTART: C:/Users/HP/Desktop/project/python practice/day2-file3.py =====
enter a value: 12
enter b value: 13
12 13 <class 'int'>
addition of two values: 25
>>> 
