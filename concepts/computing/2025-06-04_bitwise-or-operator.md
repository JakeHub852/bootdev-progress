````markdown

## Bitwise `|` Operator

The bitwise **OR** operator (`|`) works on **binary** values rather than boolean ones. It compares each bit of two numbers and returns a new binary number where each bit is `1` if **either** of the input bits is `1`.

Think of it as running multiple logical `or` operations in parallel across each bit.
````
### Example 1: `5 | 7`

```text
  0101   # 5 in binary
| 0111   # 7 in binary
  ----
  0111   # Result: 7
```

### Example 2: `5 | 2`

```text
  0101   # 5 in binary
| 0010   # 2 in binary
  ----
  0111   # Result: 7
```

### Summary

* `|` is the **bitwise OR** operator in Python.
* It returns `1` in each bit position where **either** of the bits is `1`.
* `5 | 7 == 7`
* `5 | 2 == 7`

---
