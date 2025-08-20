
---

# 🧹 Clean Code & OOP Notes

## 🎮 Course Context

This course introduces **Object-Oriented Programming (OOP)** using a game project:

> *Age of Dragons* – a real-time strategy game inspired by *Age of Empires* and *StarCraft*, where players control armies of humans, elves, orcs, and dragons.

OOP is just one way of writing code — not everyone agrees it’s the “best,” but it’s an important paradigm to understand as an engineer.

---

## 🧼 Clean Code

### What is Clean Code?

* Code that’s easy for **humans** (not just computers) to read and work with.
* Keeps programmers sane when debugging or extending software.

> *“Any fool can write code that a computer can understand.
> Good programmers write code that humans can understand.”*
> — Martin Fowler

---

### ❌ Clean Code Does *Not*:

* Make programs run faster
* Guarantee correctness
* Only exist in OOP

### ✅ Clean Code *Does*:

* Make code easier to work with
* Help find and fix bugs faster
* Speed up the development process overall
* Preserve your sanity

---

## ♻️ DRY Principle (Don’t Repeat Yourself)

### The Rule

> Avoid writing the **same code** in multiple places.

Why?

* If logic changes, you must update it **everywhere**
* Missing one update = **bugs**
* Repetition = more work, harder to maintain

---

### Example: Before Refactor

```python
soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
```

### Example: After Refactor (DRY applied)

```python
def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]

soldier_one_dps = get_soldier_dps(soldier_one)
soldier_two_dps = get_soldier_dps(soldier_two)
```

---

### Why This Matters

* If a coworker (looking at you, Allan 👀) renames the key `"damage"` to `"dmg"`:

  * **Without DRY:** You’d need to update it in **two+ places**.
  * **With DRY:** Only update **one function**, and it propagates everywhere.

> Repetition might seem harmless with 2 lines side-by-side.
> But scale it up to **hundreds of uses across dozens of files**,
> and DRY becomes essential.

---

## 📌 Key Takeaways

* **Clean code = code humans can read.**
* **DRY = centralize logic, don’t duplicate.**
* Clean, maintainable code saves future-you (and your team) a lot of pain.

---

