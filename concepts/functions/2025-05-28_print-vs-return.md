
---

## Printing vs. Returning in Functions

Understanding the difference between `print()` and `return` is **crucial** for writing correct and testable code.

---

### 🔹 `print()`

* **Purpose**: Displays output to the **console**
* **Returns**: Nothing (just prints, doesn't give data back)
* **Use Case**: Useful for **debugging**

```python
def greet():
    print("Hello!")  # Prints to console, but returns nothing
```

---

### 🔹 `return`

* **Purpose**: Ends the function and **sends a value** back to the caller
* **Does Not Print**: The returned value must be explicitly printed if needed
* **Use Case**: Essential for writing **reusable and testable functions**

```python
def greet():
    return "Hello!"  # Returns a value, does not print it
```

```python
message = greet()
print(message)  # Now it prints "Hello!"
```

---

### ⚠️ Common Mistake

Using `print()` instead of `return` in functions that are meant to **calculate and provide a result**.
This confuses output with returned data and can cause automated tests to fail.

---

### ✅ Debugging Tip

Use `print()` while you're **testing or debugging** to check variable values and flow.

```python
def add(a, b):
    print("a:", a, "b:", b)
    return a + b
```

🧹 **Cleanup Reminder**:
Remove `print()` statements once you're done debugging, especially before submitting code (e.g., on Boot.dev).

---

