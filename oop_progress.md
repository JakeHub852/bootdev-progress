
---

# 📘 OOP Progress Log

## Chapter 1 — Clean Code & DRY Principle

**Date:** Aug 20, 2025
**Status:** ✅ Completed

### 📚 What I Learned

* Clean code is code that **humans can understand** (not just computers).
* The **DRY principle (Don’t Repeat Yourself)** is key: avoid duplicating logic.
* Refactoring = rewriting code to make it cleaner and more reusable without changing what it does.

### 📝 Assignment

Task: Update `fight_soldiers` so that DPS calculation is only written once.

* Created a helper function:

```python
def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]
```

* Replaced duplicate lines with calls to `get_soldier_dps`.
* Now, the function is cleaner and easier to maintain.

### 💡 Reflection

This was a small assignment, but it drove home how **repetition quickly becomes a problem at scale**.
Even two duplicate lines can snowball into major maintenance headaches. DRY keeps things centralized and clean.

---

