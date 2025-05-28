

---

## Where to Declare Functions

In Python, code is executed from **top to bottom**, so variables and functions must be defined **before they are used**.

---

### Variable Declaration Example

Incorrect:

```python
print(my_name)
my_name = 'Lane Wagner'
```

This will raise a `NameError` because `my_name` is used before it's defined.

Correct:

```python
my_name = 'Lane Wagner'
print(my_name)  # Lane Wagner
```

---

### Function Declaration Example

Incorrect:

```python
greet()
def greet():
    print("Hello!")
```

This will raise an error because `greet()` is called before it's defined.

Correct:

```python
def greet():
    print("Hello!")

greet()  # Hello!
```

---

### Key Point

Always declare **variables and functions before using them**. Python interprets code line-by-line, and names must be known at the time they are used.

---

## Order of Functions in Python

All functions must be defined before they are called. This might seem limiting, but there is a common structure that makes this easy to manage.

---

### Recommended Structure

Define all **helper functions** first. Then define and call a special **entry point** function—typically named `main()`—at the end of the file.

This approach ensures:

* All functions are known to the interpreter before they are used
* The code remains clean and easy to navigate

---

### Example

```python
def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

def main():
    health = 10
    armor = 5
    add_armor(health, armor)

# Call the entry point last
main()
```

---

### Summary

* Define all functions before they are used
* Use a `main()` function as the entry point
* Call `main()` at the bottom of your file

Following this pattern helps keep your Python programs organized, testable, and error-free.

---


