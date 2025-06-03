
````markdown
# 🐍 Python Basics  
📅 Date: 2025-05-26

## 📌 Variables

A variable is just a name that stores a value.

Example:

```python
my_height = 100
````

* Variable names should be descriptive.
* Use a single token: lowercase with underscores (snake\_case)
* You can store numbers, text, or other data types.

### Mathematical Operators

```python
summation = a + b      # Addition
difference = a - b     # Subtraction
product = a * b        # Multiplication
quotient = a / b       # Division
```

Use parenthesis to control the order of operations:

```python
avg = (a + b + c) / 3
```

Comments make code easier to understand but are ignored by Python:

```python
# This is a comment
```

For multi-line comments or documentation, use triple quotes:

```python
"""
This is a multi-line comment
or documentation string (docstring).
"""
```



````markdown
# Basic Variable Types

Python has several basic data types.

## Strings

In programming, snippets of text are called **strings**. They're lists of characters strung together. We create strings by wrapping the text in single quotes or double quotes. That said, **double quotes are preferred**.

```python
name_with_single_quotes = 'boot.dev'  # not so good
name_with_double_quotes = "boot.dev"  # so good
````

## Numbers

Numbers are not surrounded by quotes when they're declared.

An integer (or **int**) is a number without a decimal part:

```python
x = 5    # positive integer
y = -5   # negative integer
```

A float is a number with a decimal part:

```python
x = 5.2
y = -5.2
```

## Booleans

A **Boolean** (or **bool**) is a type that can only have one of two values: `True` or `False`. As you may have heard, computers really only use 1's and 0's. These 1's and 0's are just `True`/`False` boolean values.

```python
is_tall = True
is_short = False
```

## F' Strings in Python
In python we can create strings with dynamic values with the f'string syntax.

```python
num_bananas = 10
f_string = f"You have {num_bananas} bananas"
print(f_string)
# You have 10 bananas
```
* Opening quotes must be preceded by an f.
* Variables with curly brackets have their values 'interpolated' into the string.
* Just a string with special syntax.

## None type Variables
Not all variables have a value. We can make an "empty" variable by setting it to None. None is a special value in Python that represents the absence of a value. It is not the same as zero, False, or an empty string.

```python
my_mental_acuity = None
```
## Dynamic Typing
- Python is dynamically typed, which means a variable can store any type, and that type can change.
- In almost all circumstances, it's a bad idea to change the type of a variable. The "proper" thing to do is to just create a new one.