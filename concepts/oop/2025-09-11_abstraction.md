
---

## Abstraction vs Encapsulation

**Quick Summary**

* **Abstraction** → simplifies use by exposing only essentials
* **Encapsulation** → protects integrity by hiding internals

---

### Abstraction

* Simplifies complex behavior by exposing a clear interface
* Focuses on **what is exposed (public)**
* Goal: reduce complexity

### Encapsulation

* Hides internal state and implementation details
* Focuses on **what is hidden (private)**
* Goal: maintain integrity of internals

👉 In practice, you’re usually doing **both** at once. The terms just highlight different perspectives.

---

## Example: `random.randrange(5)`

* Random number generation is complex (hardware + OS seeds)
* The `random` library **abstracts** this complexity into a simple call
* Internal state and implementation are **encapsulated** so you don’t have to handle them

Changing `randrange`’s interface would break code everywhere → **good abstractions matter**.

---

## Why It Matters

* **Abstraction:** expose essentials, hide complexity
* **Encapsulation:** bundle data + methods, restrict direct access
* Both → easier to use, safer to maintain

Example: Python’s `pow` abstracts exponentiation:

```python
def pow(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
```

The real implementation is more efficient, but the interface stays simple.

---

**Essence:** abstraction simplifies the outside, encapsulation protects the inside.

---

