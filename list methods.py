>>> # List methods , methods are like functions but they are called within a variable
>>> spam = ['Hello ' , ' Hi ' , 'Howdy ' , ' Heyas ' ]
>>> spame.index('hello')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    spame.index('hello')
NameError: name 'spame' is not defined
>>> spame.index('Hello')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    spame.index('Hello')
NameError: name 'spame' is not defined
>>> spam.index(' Hi ' )
1
>>> spame.index('Hello ' )
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    spame.index('Hello ' )
NameError: name 'spame' is not defined
>>> spam.index('Hello '  )
0
>>> # The index methods finds the element inside a list
>>> # To add new values to a list we use insert or append method :
>>> spam = [ 'Cat' , 'dog' , 'bat' ]
>>> spam.append('moose')
>>> spame
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    spame
NameError: name 'spame' is not defined
>>> spam
['Cat', 'dog', 'bat', 'moose']
>>> spam.insert(1,'chicken')
>>> spam
['Cat', 'chicken', 'dog', 'bat', 'moose']
>>> spam.remove('dog')
>>> spam
['Cat', 'chicken', 'bat', 'moose']
>>> #remove element from a list using remove method
>>> del spam[0]
>>> spam
['chicken', 'bat', 'moose']
>>> # the delete function is used to delete an element by using its position
>>> spam = [2,5,3.14,-7]
>>> spam.sort()
>>> spam
[-7, 2, 3.14, 5]
>>> #sort method is used to sequence the list elements
>>> spam = [ 'ants' , 'cats' , 'dogs' ]
>>> spam.sort()
>>> spam
['ants', 'cats', 'dogs']
>>> spam.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    spam.sort(reverse=true)
NameError: name 'true' is not defined
>>> spam.sort(reverse=True)
>>> spam
['dogs', 'cats', 'ants']
>>> 
