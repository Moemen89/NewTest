>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> supplies = [ 'pens' , 'staplers' , 'flame-throweres' , 'binder' ]
>>> for i in range(len(supplies)) :
	print ( 'Index ' + str(i) + ' in supplies is ' + supplies[i] )

	
Index 0 in supplies is pens
Index 1 in supplies is staplers
Index 2 in supplies is flame-throweres
Index 3 in supplies is binder
>>> len(supplies)
4
>>> #we can assign multiple values in the same time instead of wrinting the code many times :
>>> cat = ['fat' ,'orange ' , ' loud ' ]
>>> color = cat[0]
>>> size = cat[1]
>>> disposition = cat[2]
>>> #instead i can do this :
>>> size,color,dispostion = cat
>>> size
'fat'
>>> color
'orange '
>>> dispotion
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dispotion
NameError: name 'dispotion' is not defined
>>> dispostion
' loud '
>>> size ,color,dispostion = 'skinny' , 'black ','quiet'
>>> #swapping variables :
>>> a = 'aaa'
>>> b = 'bbb'
>>> a,b = b,a
>>> a
'bbb'
>>> b
'aaa'
>>> 
