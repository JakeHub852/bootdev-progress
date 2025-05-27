
---

# 🔄 Dynamic Typing in Python

## 📌 What is Dynamic Typing?

* Python is **dynamically typed**, meaning:

  * **Variables don't have fixed types.**
  * You can assign **any type of value** to a variable.
  * The **type can change** during runtime.

```python
speed = 5         # speed is an integer
speed = "five"    # now it's a string
```

---

## ⚠️ But Maybe Don't...

While it's *possible* to change a variable's type, it's usually a **bad practice**.

✅ Instead, use **new variables** for clarity and safety:

```python
speed = 5
speed_description = "five"
```

---

## 🔒 Static Typing (for Comparison)

* **Statically typed** languages (like **Go**, **Java**, **C**):

  * Variables have **fixed types**.
  * Type must be **declared** or inferred at the start.
  * Trying to assign the wrong type causes a **compile-time error**.

```go
int speed = 5
speed = "five"  // ❌ Error: cannot assign string to int
```

---

## 🧠 Summary

| Concept          | Dynamic Typing (Python) | Static Typing (e.g., Go)    |
| ---------------- | ----------------------- | --------------------------- |
| Variable Type    | Can change at runtime   | Fixed at declaration        |
| Type Declaration | Not required            | Required or inferred        |
| Flexibility      | High                    | Lower, but more predictable |
| Error Detection  | At runtime              | At compile time             |

* ✔ Use dynamic typing **responsibly** to keep code clean and readable.
* ❌ Avoid changing variable types mid-code unless there's a compelling reason.

---