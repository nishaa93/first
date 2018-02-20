Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> 
>>> import numpy as np
>>> import pandas as pd
>>> s=pd.series([1,3,5,np.nan,6,8])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s=pd.series([1,3,5,np.nan,6,8])
AttributeError: module 'pandas' has no attribute 'series'
>>> s = pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates = pd.date_range('20130101',periods=6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> dates = pd.date_range('20180216',periods=10)
>>> dates
SyntaxError: multiple statements found while compiling a single statement
>>> AttributeError: module 'pandas' has no attribute 'series'
SyntaxError: invalid syntax
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df2 = pd.DataFrame({ 'A' : 1.,
   ....:                      'B' : pd.Timestamp('20130102'),
   ....:                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
   ....:                      'D' : np.array([3] * 4,dtype='int32'),
   ....:                      'E' : pd.Categorical(["test","train","test","train"]),
   ....:                      'F' : 'foo' })
   ....:
	   
SyntaxError: invalid syntax
>>> df2 = pd.DataFrame({ 'A' : 1.,
   ...                      'B' : pd.Timestamp('20130102'),
   ...                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
   ...                      'D' : np.array([3] * 4,dtype='int32'),
   ...                      'E' : pd.Categorical(["test","train","test","train"]),
   ...                      'F' : 'foo' })
   ...
   
SyntaxError: invalid syntax
>>> 
>>> df2 = pd.DataFrame({ 'A' : 1.,
                        'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                        'D' : np.array([3] * 4,dtype='int32'),
                        'E' : pd.Categorical(["test","train","test","train"]),
                        'F' : 'foo' })
>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> f=pd.Timestamp('20180216)
		   
SyntaxError: EOL while scanning string literal
>>> f=pd.Timestamp('20180216')
		   
>>> f
		   
Timestamp('2018-02-16 00:00:00')
>>> f=pd.Categorical(['male','female'])
		   
>>> f
		   
[male, female]
Categories (2, object): [female, male]
>>> df2.dtypes
		   
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
>>> 
KeyboardInterrupt
>>> df.index
		   
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    df.index
NameError: name 'df' is not defined
>>> df.index
		   
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    df.index
NameError: name 'df' is not defined
>>> df2.index
		   
Int64Index([0, 1, 2, 3], dtype='int64')
>>> df2.columns
		   
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
>>> df2
		   
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> d2.T
		   
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d2.T
NameError: name 'd2' is not defined
>>> df2.T
		   
                     0                    1                    2  \
A                    1                    1                    1   
B  2013-01-02 00:00:00  2013-01-02 00:00:00  2013-01-02 00:00:00   
C                    1                    1                    1   
D                    3                    3                    3   
E                 test                train                 test   
F                  foo                  foo                  foo   

                     3  
A                    1  
B  2013-01-02 00:00:00  
C                    1  
D                    3  
E                train  
F                  foo  
>>> df.T
		   
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    df.T
NameError: name 'df' is not defined
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
		   
>>> df.T
		   
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A   -0.524023   -1.223878   -0.136757    1.311967   -0.276603   -1.317268
B    0.191322    1.916285   -0.912929   -0.358749   -0.329019   -0.264223
C    0.167914    0.498380   -0.773541    2.327185    0.404259   -2.027346
D    0.720313   -1.249180    1.638123    1.152543   -0.711160   -0.875184
>>> df.T
		   
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A   -0.524023   -1.223878   -0.136757    1.311967   -0.276603   -1.317268
B    0.191322    1.916285   -0.912929   -0.358749   -0.329019   -0.264223
C    0.167914    0.498380   -0.773541    2.327185    0.404259   -2.027346
D    0.720313   -1.249180    1.638123    1.152543   -0.711160   -0.875184
>>> df.sort_index(axis=1,ascending=False)
		   
                   D         C         B         A
2013-01-01  0.720313  0.167914  0.191322 -0.524023
2013-01-02 -1.249180  0.498380  1.916285 -1.223878
2013-01-03  1.638123 -0.773541 -0.912929 -0.136757
2013-01-04  1.152543  2.327185 -0.358749  1.311967
2013-01-05 -0.711160  0.404259 -0.329019 -0.276603
2013-01-06 -0.875184 -2.027346 -0.264223 -1.317268
>>> df.T
		   
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A   -0.524023   -1.223878   -0.136757    1.311967   -0.276603   -1.317268
B    0.191322    1.916285   -0.912929   -0.358749   -0.329019   -0.264223
C    0.167914    0.498380   -0.773541    2.327185    0.404259   -2.027346
D    0.720313   -1.249180    1.638123    1.152543   -0.711160   -0.875184
>>> df.sort_values(by='A')
		   
                   A         B         C         D
2013-01-06 -1.317268 -0.264223 -2.027346 -0.875184
2013-01-02 -1.223878  1.916285  0.498380 -1.249180
2013-01-01 -0.524023  0.191322  0.167914  0.720313
2013-01-05 -0.276603 -0.329019  0.404259 -0.711160
2013-01-03 -0.136757 -0.912929 -0.773541  1.638123
2013-01-04  1.311967 -0.358749  2.327185  1.152543
>>> df[0:3]
		   
                   A         B         C         D
2013-01-01 -0.524023  0.191322  0.167914  0.720313
2013-01-02 -1.223878  1.916285  0.498380 -1.249180
2013-01-03 -0.136757 -0.912929 -0.773541  1.638123
>>> df.loc[dates[0]]
		   
A   -0.524023
B    0.191322
C    0.167914
D    0.720313
Name: 2013-01-01 00:00:00, dtype: float64
>>> 
