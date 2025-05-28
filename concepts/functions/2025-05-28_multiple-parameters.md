
---

## Functions with Multiple Parameters

Functions can accept **more than one parameter** (input). This allows for more flexible and powerful code.

### Example: Subtract Function

```python
def subtract(a, b):
    result = a - b
    return result
```

#### Function Call

```python
result = subtract(5, 3)
print(result)  # 2
```

* `a = 5`, `b = 3`
* Returns `5 - 3 = 2`

> 🔑 **Note**: Parameter **position** matters, not the names.
> The first value goes to the first parameter, the second to the second, and so on.

---

### Example: Introduction Function

```python
def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro
```

#### Function Call

```python
my_name = "John"
my_age = "30"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro)
# Your name is John and you are 30 years old. You are 1.8 meters tall and weigh 80 kilograms.
```

---

### Summary

* Functions can take **multiple inputs**.
* Values are assigned based on their **position**, not their name.
* Useful for organizing related pieces of data into reusable logic.

---

