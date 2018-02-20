Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
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
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
>>> df2.<TAB>
SyntaxError: invalid syntax
>>> df2.<TAB>
SyntaxError: invalid syntax
>>> df.head()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    df.head()
NameError: name 'df' is not defined
>>> NameError: name 'df' is not defined
SyntaxError: invalid syntax
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
NameError: name 'dates' is not defined
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
NameError: name 'dates' is not defined
>>> dates = pd.date_range('20130101', periods=6)

>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
>>> df
                   A         B         C         D
2013-01-01  0.263000  0.549562  0.706085 -1.033819
2013-01-02 -0.752599  2.851744 -0.709823 -0.161485
2013-01-03  1.928684 -0.357733 -1.453943 -1.039202
2013-01-04 -1.556657 -0.111249  0.370461 -1.521161
2013-01-05  0.111378 -0.318333  1.201091 -0.726234
2013-01-06 -1.173002 -0.250931  0.624886 -0.442425
>>> df.head()
                   A         B         C         D
2013-01-01  0.263000  0.549562  0.706085 -1.033819
2013-01-02 -0.752599  2.851744 -0.709823 -0.161485
2013-01-03  1.928684 -0.357733 -1.453943 -1.039202
2013-01-04 -1.556657 -0.111249  0.370461 -1.521161
2013-01-05  0.111378 -0.318333  1.201091 -0.726234
>>> df.tail(3)
                   A         B         C         D
2013-01-04 -1.556657 -0.111249  0.370461 -1.521161
2013-01-05  0.111378 -0.318333  1.201091 -0.726234
2013-01-06 -1.173002 -0.250931  0.624886 -0.442425
>>> df,index()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    df,index()
NameError: name 'index' is not defined
>>> df.index()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    df.index()
TypeError: 'DatetimeIndex' object is not callable
>>> df.index
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')
>>> df.describe
<bound method NDFrame.describe of                    A         B         C         D
2013-01-01  0.263000  0.549562  0.706085 -1.033819
2013-01-02 -0.752599  2.851744 -0.709823 -0.161485
2013-01-03  1.928684 -0.357733 -1.453943 -1.039202
2013-01-04 -1.556657 -0.111249  0.370461 -1.521161
2013-01-05  0.111378 -0.318333  1.201091 -0.726234
2013-01-06 -1.173002 -0.250931  0.624886 -0.442425>
>>> df.T
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.263000   -0.752599    1.928684   -1.556657    0.111378   -1.173002
B    0.549562    2.851744   -0.357733   -0.111249   -0.318333   -0.250931
C    0.706085   -0.709823   -1.453943    0.370461    1.201091    0.624886
D   -1.033819   -0.161485   -1.039202   -1.521161   -0.726234   -0.442425
>>> df.sort_index(axis=1, ascending=False)
                   D         C         B         A
2013-01-01 -1.033819  0.706085  0.549562  0.263000
2013-01-02 -0.161485 -0.709823  2.851744 -0.752599
2013-01-03 -1.039202 -1.453943 -0.357733  1.928684
2013-01-04 -1.521161  0.370461 -0.111249 -1.556657
2013-01-05 -0.726234  1.201091 -0.318333  0.111378
2013-01-06 -0.442425  0.624886 -0.250931 -1.173002
>>> df.sort_values(by='B')
                   A         B         C         D
2013-01-03  1.928684 -0.357733 -1.453943 -1.039202
2013-01-05  0.111378 -0.318333  1.201091 -0.726234
2013-01-06 -1.173002 -0.250931  0.624886 -0.442425
2013-01-04 -1.556657 -0.111249  0.370461 -1.521161
2013-01-01  0.263000  0.549562  0.706085 -1.033819
2013-01-02 -0.752599  2.851744 -0.709823 -0.161485
>>> df['A']
2013-01-01    0.263000
2013-01-02   -0.752599
2013-01-03    1.928684
2013-01-04   -1.556657
2013-01-05    0.111378
2013-01-06   -1.173002
Freq: D, Name: A, dtype: float64
>>> df[0:3]
                   A         B         C         D
2013-01-01  0.263000  0.549562  0.706085 -1.033819
2013-01-02 -0.752599  2.851744 -0.709823 -0.161485
2013-01-03  1.928684 -0.357733 -1.453943 -1.039202
>>> df['20130102':'20130104']
                   A         B         C         D
2013-01-02 -0.752599  2.851744 -0.709823 -0.161485
2013-01-03  1.928684 -0.357733 -1.453943 -1.039202
2013-01-04 -1.556657 -0.111249  0.370461 -1.521161
>>>  df.loc[dates[0]]
SyntaxError: unexpected indent
>>> df.loc[dates[0]]
A    0.263000
B    0.549562
C    0.706085
D   -1.033819
Name: 2013-01-01 00:00:00, dtype: float64
>>> df.loc[:,['A','B']]
                   A         B
2013-01-01  0.263000  0.549562
2013-01-02 -0.752599  2.851744
2013-01-03  1.928684 -0.357733
2013-01-04 -1.556657 -0.111249
2013-01-05  0.111378 -0.318333
2013-01-06 -1.173002 -0.250931
>>> 
KeyboardInterrupt
>>>  df.loc['20130102':'20130104',['A','B']]
SyntaxError: unexpected indent
>>> df.loc['20130102':'20130104',['A','B']]
                   A         B
2013-01-02 -0.752599  2.851744
2013-01-03  1.928684 -0.357733
2013-01-04 -1.556657 -0.111249
>>> df.loc['20130102',['A','B']]
A   -0.752599
B    2.851744
Name: 2013-01-02 00:00:00, dtype: float64
>>> df.loc[dates[0],'A']
0.2630002291014032
>>> df.at[dates[0],'A']
0.2630002291014032
>>> 
