
---

## Functions – Reusing Code

Functions allow us to **organize** and **reuse** code, which is especially useful when performing the same task multiple times (like calculating the area of circles with different radii).

### Problem Without Functions

```python
radius = 5
area1 = 3.14 * radius * radius

radius2 = 7
area2 = 3.14 * radius2 * radius2
```

This works, but it's **inefficient** and **repetitive**, especially if we need to calculate the area of many circles.

---

### Solution: Define a Function

```python
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result
```

#### Function Breakdown:

* `area_of_circle` is the function name.
* `r` is the **parameter** (input).
* The **body** is indented and runs every time we call the function.
* The function **returns** the calculated result.

---

### Using the Function

```python
area = area_of_circle(5)
print(area)  # 78.5
```

* `5` is passed in as `r`
* Function calculates `3.14 * 5 * 5`
* Returns `78.5`, which is stored in `area`

---

### Reusability

```python
print(area_of_circle(6))  # 113.04
print(area_of_circle(7))  # 153.86
```

We can now calculate the area for any circle just by calling `area_of_circle()` with a different radius.



````markdown
# Python: Default Function Arguments

In Python, you can specify default values for function arguments. This is useful for making some parameters optional.

## Syntax

Default values are set using the assignment (`=`) operator in the function signature:

```python
def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)
````

## Examples

```python
get_greeting("lane@example.com", "Lane")
# Output: Hello Lane welcome! You've registered your email: lane@example.com

get_greeting("lane@example.com")
# Output: Hello there welcome! You've registered your email: lane@example.com
```

## Notes

* Parameters with default values must come **after** all required parameters.
* Default values are used when the caller omits the argument.





