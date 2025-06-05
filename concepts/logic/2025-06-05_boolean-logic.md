

````markdown
# Boolean Logic

Boolean logic refers to logic dealing with boolean values — `True` or `False`.

### Examples

- **Dogs must have four legs _and_ weigh less than 100 kilograms.**  
  → Both conditions must be true.

- **Cars are cool if they go faster than 200 MPH _or_ if they are electric.**  
  → At least one condition must be true.

---

## Logical Operators Review

Python provides two common logical operators for boolean logic:

- `and` – Returns `True` if **both** conditions are `True`.
- `or` – Returns `True` if **at least one** condition is `True`.

---

## `and` Operator

The `and` operator returns `True` only if **both** conditions evaluate to `True`.
````
```python
def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100
````
### Example 1

```python
is_dog(4, 99)
```

Evaluation:

```
return 4 == 4 and 99 < 100
return True and True
return True
```

### Example 2

```python
is_dog(3, 98)
```

Evaluation:

```
return 3 == 4 and 98 < 100
return False and True
return False
```

---

## `or` Operator

The `or` operator returns `True` if **at least one** condition evaluates to `True`.

```python
def is_car_cool(speed, is_electric):
    return speed > 200 or is_electric
```

### Example

```python
is_car_cool(250, False)
```

Evaluation:

```
return 250 > 200 or False
return True or False
return True
````