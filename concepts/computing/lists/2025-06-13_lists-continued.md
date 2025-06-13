## Python Lists Overview

### Finding the Maximum Value

To find the maximum value in a list, a common technique is to start with a baseline value that will be lower than any possible number in the list. Instead of using arbitrary values like `0` or `-100000`, Python provides a better option:

```python
negative_infinity = float("-inf")
```

* `float("-inf")` represents **negative infinity**, which is smaller than any other number.
* This makes it a perfect starting point for comparisons when searching for the **maximum** value in a list.
* Similarly, `float("inf")` can be used for **positive infinity** when looking for a minimum.

```python
positive_infinity = float("inf")
```

---

### Modulo Operator in Python

The **modulo operator** (`%`) is used to find the **remainder** of a division operation.

#### Example:

```python
7 % 2  # Result: 1
```

* `2 * 3 = 6`
* `7 - 6 = 1` → So, the remainder is `1`.

```python
remainder = 8 % 3  # remainder = 2
```

> Note: The `%` symbol **does not** represent a percentage. It is used for modulo operations only.

#### Use Case: Checking for Odd Numbers

```python
if number % 2 != 0:
    print("This is an odd number.")
```

An **odd number** is one where the remainder when divided by 2 is **not zero**.

---

### Slicing Lists

Python allows for easy slicing of lists using the **colon (`:`) operator**. This is helpful when you want to work with only a specific part of a list.

#### Syntax:

```python
my_list[start : stop : step]
```

* `start`: The index to begin the slice (inclusive).
* `stop`: The index to end the slice (exclusive).
* `step`: How many elements to skip each time.

#### Example:

```python
scores = [50, 70, 30, 20, 90, 10, 50]
print(scores[1:5:2])  # Output: [70, 20]
```

This reads as: "Get a slice from index 1 up to (but not including) index 5, skipping every second element."

#### Omitting Sections

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[:3]   # [0, 1, 2]     → From start to index 3 (exclusive)
numbers[3:]   # [3, 4, 5, 6, 7, 8, 9] → From index 3 to the end
numbers[::2]  # [0, 2, 4, 6, 8] → Every second element from start to end
```

#### Negative Indices

Negative indices allow you to access elements from the end of the list:

```python
numbers[-1]   # 9   → Last element
numbers[-2]   # 8   → Second last element
numbers[-3:]  # [7, 8, 9] → Last three elements
```

List slicing always returns a **new list** without modifying the original.

---

### List Operations – Concatenation

You can **concatenate** (combine) two or more lists in Python using the `+` operator.

#### Example:

```python
total = [1, 2, 3] + [4, 5, 6]
print(total)  # Output: [1, 2, 3, 4, 5, 6]
```

The `+` operator returns a **new list** that contains all the elements from both lists in order.

---

### List Operations – Checking for Membership

To check whether a value **exists** in a list, use the `in` keyword. To check that a value **does not exist**, use `not in`.

#### Examples:

```python
fruits = ["apple", "orange", "banana"]

print("banana" in fruits)     # Output: True
print("banana" not in fruits) # Output: False
```

These expressions return Boolean values (`True` or `False`) and are commonly used in conditionals.

---

### List Deletion

Python provides the built-in `del` keyword to **delete elements** from a list. You can delete:

* A single item by index
* A slice (range) of items
* All elements in the list

#### Examples:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Delete the fourth item (index 3)
del nums[3]
print(nums)  # Output: [1, 2, 3, 5, 6, 7, 8, 9]

# Delete the second to third item (indices 1 to 2)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)  # Output: [1, 4, 5, 6, 7, 8, 9]

# Delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)  # Output: []
```

The `del` operation modifies the list in place.

---
