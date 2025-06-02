````markdown
## Logical Operators
````
You're probably familiar with the logical operators ``and`` and ``or``.

Logical operators deal with boolean values, ``True`` and ``False``.

The logical ``and`` operator requires that both inputs are ``True`` to return ``True``. The logical or operator only requires that at least one input is ``True`` to return ``True``.

For example:
````python
True and True == True
True and False == False
False and False == False

True or True == True
True or False == True
False or False == False
````
## Python Syntax
````python
print(True and True)
# prints True

print(True or False)
# prints True
````
## Nesting With Parentheses
We can nest logical expressions using parentheses.
````python
print((True or False) and False)
````
First, we evaluate the expression in the parentheses, ``(True or False)``. It evaluates to ``True``:
````python
print(True and False)
````
``True and False`` evaluates to ``False:``
```python
print(False)
````
So, ``print((True or False) and False)`` prints "False" to the console.
````markdown 
# Not 
````
We skipped a very important logical operator - ``not``. The ``not`` operator reverses the result. It returns ``False`` if the output is ``True`` and vice-versa.
````python
print(not True)
# Prints: False

print(not False)
# Prints: True
````
