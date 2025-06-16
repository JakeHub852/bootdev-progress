# Errors and Exceptions in Python

In Python, errors fall into two main categories:

* **Syntax Errors** – Errors in the structure of the code.
* **Exceptions** – Errors that occur during execution.

---

## 1. Syntax Errors

A **syntax error** occurs when the code violates the grammar rules of Python.

Example:

```python
this is not valid code, so it will error
```

Trying to run the above line results in:

```
SyntaxError: invalid syntax
```

---

## 2. Exceptions

Exceptions are errors that occur **during program execution**, even if the code has valid syntax.

### 2.1 Basic Exception Handling

Python handles exceptions using `try` and `except` blocks:

```python
try:
    10 / 0
except Exception:
    print("can't divide by zero")
```

* The `try` block runs until an error occurs.
* If an exception is raised, the `except` block executes.
* If no error occurs, the `except` block is skipped.

### 2.2 Accessing the Exception Object

To access exception details:

```python
try:
    10 / 0
except Exception as e:
    print(e)
# Output: division by zero
```

---

## 3. Raising Your Own Exceptions

Developers should raise exceptions when invalid or unexpected behavior occurs.

> An error is **not a bug** if it's expected and handled gracefully.

### 3.1 Example

```python
def craft_sword(metal_bar):
    if metal_bar == "bronze":
        return "bronze sword"
    if metal_bar == "iron":
        return "iron sword"
    if metal_bar == "steel":
        return "steel sword"
    raise Exception("invalid metal bar")
```

This raises an exception if the input is not one of the supported materials.

---

## 4. Best Practices

### 4.1 Don't Catch Your Own Exceptions

Avoid catching exceptions in the same function that raises them. Let the caller handle it.

#### ❌ Bad Practice

```python
def craft_sword(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        if metal_bar == "iron":
            return "iron sword"
        if metal_bar == "steel":
            return "steel sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")
```

#### ✅ Good Practice

```python
try:
    craft_sword("gold bar")
except Exception as e:
    print(e)
```

---

## 5. Raising Exceptions: Review

Applications are not immune to:

* Network issues
* Missing data
* Memory limits
* Invalid inputs

Despite testing, failures **will happen**. Your job as a developer is to:

* **Catch exceptions** before they crash the program.
* **Raise exceptions** when something goes wrong in your logic.

Example:

```python
raise Exception("something bad happened")
```

This clearly signals a controlled error and enables clean error handling.

---

## 6. Different Types of Exceptions

Although we haven't covered classes and objects yet (which underlie how exceptions work), it's important to understand that there are **different types of exceptions**, each suited to different error situations.

Some common examples:

* `ZeroDivisionError`: Raised when dividing by zero.
* `IndexError`: Raised when accessing an invalid index in a list.
* `Exception`: The base class for all exceptions.

### 6.1 Handling Specific Exceptions

You can handle specific exceptions before falling back to a more general one:

```python
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)
```

Output:

```
0 division
index error
```

### 6.2 Why Specific Exceptions Come First

Always handle the most specific exceptions **before** general ones, because Python stops checking as soon as it finds a match.

#### Example:

```python
try:
    nums = [0, 1]
    print(nums[2])
except Exception:
    print("An error occurred")
except IndexError:
    print("Index error")
```

This prints:

```
An error occurred
```

Because `Exception` catches the error before `IndexError` is reached.

### 6.3 Using Exception Aliases

You can access the error message using `as`, like this:

```python
except Exception as e:
    print(e)
```

This prints the string representation of the exception, which is helpful for debugging.

---
